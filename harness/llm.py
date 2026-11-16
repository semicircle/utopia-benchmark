"""Model clients for the Utopia harness.

Two providers, chosen with --provider:

  anthropic  the Anthropic Messages API (official `anthropic` SDK). --base-url
             works for any Messages-compatible gateway.
  openai     any OpenAI-compatible Chat Completions endpoint (official `openai`
             SDK): OpenAI, OpenRouter, Together, vLLM, Ollama, LM Studio, ...

Both expose the same two operations:

  oneshot(system, prompt)                 one request, no tools
  agent(system, prompt, tools, limits)    a tool-use loop; tools run locally

Every model gets the same three tools (run_shell, read_file, write_file), so
results are comparable across providers. Usage is accumulated per run and
priced from PRICES (or --price-in/--price-out) to enforce a USD budget.
"""

import json
import time

# USD per million tokens: input, output, cache read, cache write (5 minute TTL).
PRICES = {
    "claude-fable-5-2": (8.00, 40.00, 0.20, 10.00),
    "claude-opus-5-5": (4.00, 20.00, 0.20, 5.00),
    "claude-opus-5": (5.00, 25.00, 0.50, 6.25),
    "claude-sonnet-5-5": (2.00, 10.00, 0.10, 2.50),
    "claude-sonnet-5": (2.00, 10.00, 0.20, 2.50),
    "claude-haiku-5-5": (0.10, 0.50, 0.01, 0.125),
}

TOOLS = [
    {
        "name": "run_shell",
        "description": ("Run a shell command (bash) in the workspace directory and return its exit "
                        "status, standard output and standard error. Each call starts a fresh shell "
                        "in the workspace; there is no internet access. Commands time out after 30 seconds."),
        "schema": {
            "type": "object",
            "properties": {"command": {"type": "string", "description": "the command to run"}},
            "required": ["command"],
            "additionalProperties": False,
        },
    },
    {
        "name": "read_file",
        "description": "Read a text file in the workspace. The path is relative to the workspace.",
        "schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}},
            "required": ["path"],
            "additionalProperties": False,
        },
    },
    {
        "name": "write_file",
        "description": ("Create or overwrite a text file in the workspace with the given content. "
                        "The path is relative to the workspace; parent directories are created."),
        "schema": {
            "type": "object",
            "properties": {"path": {"type": "string"}, "content": {"type": "string"}},
            "required": ["path", "content"],
            "additionalProperties": False,
        },
    },
]


class Limits:
    def __init__(self, max_steps=150, max_cost=None, max_seconds=3600):
        self.max_steps, self.max_cost, self.max_seconds = max_steps, max_cost, max_seconds


class Usage:
    """Token counts accumulated over every request of a run."""

    def __init__(self, model, price_in=None, price_out=None):
        p = PRICES.get(model)
        if price_in is not None and price_out is not None:
            p = (price_in, price_out, price_in * 0.1, price_in * 1.25)
        self.prices = p
        self.input = self.output = self.cache_read = self.cache_write = 0
        self.requests = 0

    def add(self, input=0, output=0, cache_read=0, cache_write=0):
        self.input += input or 0
        self.output += output or 0
        self.cache_read += cache_read or 0
        self.cache_write += cache_write or 0
        self.requests += 1

    def cost(self):
        if not self.prices:
            return None
        pi, po, pr, pw = self.prices
        return (self.input * pi + self.output * po + self.cache_read * pr + self.cache_write * pw) / 1e6

    def to_dict(self):
        c = self.cost()
        return {
            "input_tokens": self.input, "output_tokens": self.output,
            "cache_read_input_tokens": self.cache_read, "cache_creation_input_tokens": self.cache_write,
            "requests": self.requests,
            "cost_usd_estimate": None if c is None else round(c, 4),
        }


class ProviderError(RuntimeError):
    pass


def make_client(provider, model, api_key, base_url=None, effort=None, thinking=True,
                max_tokens=32000, price_in=None, price_out=None):
    if provider == "anthropic":
        return AnthropicClient(model, api_key, base_url, effort, thinking, max_tokens, price_in, price_out)
    if provider == "openai":
        return OpenAIClient(model, api_key, base_url, effort, max_tokens, price_in, price_out)
    raise ValueError(f"unknown provider {provider!r}")


def _stop_reason_for(limits, steps, usage, started):
    if steps >= limits.max_steps:
        return "max_steps"
    c = usage.cost()
    if limits.max_cost is not None and c is not None and c >= limits.max_cost:
        return "max_cost"
    if time.time() - started >= limits.max_seconds:
        return "max_seconds"
    return None


# ---------------------------------------------------------------- Anthropic

class AnthropicClient:
    def __init__(self, model, api_key, base_url, effort, thinking, max_tokens, price_in, price_out):
        import anthropic
        self.anthropic = anthropic
        self.client = anthropic.Anthropic(api_key=api_key, base_url=base_url, max_retries=4,
                                          timeout=900.0)
        self.model, self.effort, self.thinking, self.max_tokens = model, effort, thinking, max_tokens
        self.price_in, self.price_out = price_in, price_out

    def _params(self, system, messages, tools=None):
        p = {
            "model": self.model,
            "max_tokens": self.max_tokens,
            "system": system,
            "messages": messages,
            # Cache the growing conversation prefix: agent loops resend it every turn.
            "cache_control": {"type": "ephemeral"},
        }
        # Refusal fallbacks are deliberately NOT enabled: a benchmark score must
        # come from the model under test, not from a fallback model.
        if self.thinking:
            p["thinking"] = {"type": "adaptive"}
        if self.effort:
            p["output_config"] = {"effort": self.effort}
        if tools:
            p["tools"] = [{"name": t["name"], "description": t["description"], "input_schema": t["schema"]}
                          for t in tools]
        return p

    def _call(self, params, usage):
        a = self.anthropic
        try:
            with self.client.messages.stream(**params) as stream:
                msg = stream.get_final_message()
        except a.AuthenticationError as e:
            raise ProviderError(f"authentication failed: {e.message}") from e
        except a.PermissionDeniedError as e:
            raise ProviderError(f"permission denied: {e.message}") from e
        except a.BadRequestError as e:
            raise ProviderError(f"bad request: {e.message}") from e
        except a.NotFoundError as e:
            raise ProviderError(f"not found (model or endpoint): {e.message}") from e
        except a.APIStatusError as e:
            raise ProviderError(f"API error {e.status_code}: {e.message}") from e
        except a.APIConnectionError as e:
            raise ProviderError(f"connection error: {e}") from e
        u = msg.usage
        usage.add(u.input_tokens, u.output_tokens, getattr(u, "cache_read_input_tokens", 0),
                  getattr(u, "cache_creation_input_tokens", 0))
        return msg

    def oneshot(self, system, prompt):
        usage = Usage(self.model, self.price_in, self.price_out)
        msg = self._call(self._params(system, [{"role": "user", "content": prompt}]), usage)
        text = "".join(b.text for b in msg.content if b.type == "text")
        return {"text": text, "stop_reason": msg.stop_reason, "usage": usage.to_dict(),
                "raw": msg.to_dict()}

    def agent(self, system, prompt, tools, execute, limits, log):
        usage = Usage(self.model, self.price_in, self.price_out)
        messages = [{"role": "user", "content": prompt}]
        log({"type": "user", "content": prompt})
        started, steps, final_text, stop = time.time(), 0, "", None
        while True:
            stop = _stop_reason_for(limits, steps, usage, started)
            if stop:
                break
            msg = self._call(self._params(system, messages, tools), usage)
            steps += 1
            log({"type": "assistant", "step": steps, "message": msg.to_dict(), "usage_so_far": usage.to_dict()})
            # Append the content unchanged (thinking blocks included).
            messages.append({"role": "assistant", "content": msg.content})
            if msg.stop_reason == "refusal":
                stop = "refusal"
                break
            calls = [b for b in msg.content if b.type == "tool_use"]
            final_text = "".join(b.text for b in msg.content if b.type == "text") or final_text
            if msg.stop_reason == "max_tokens" and calls:
                # A truncated tool call cannot be run; ask the model to continue.
                messages.append({"role": "user", "content": [
                    {"type": "tool_result", "tool_use_id": c.id, "is_error": True,
                     "content": "Your output was cut off by the token limit before this call was complete. Try again with a shorter step."}
                    for c in calls]})
                continue
            if not calls:
                if msg.stop_reason == "pause_turn":
                    continue
                stop = "end_turn"
                break
            results = []
            for c in calls:
                out, is_error = execute(c.name, c.input)
                log({"type": "tool_result", "tool": c.name, "input": c.input, "output": out, "is_error": is_error})
                results.append({"type": "tool_result", "tool_use_id": c.id, "content": out, "is_error": is_error})
            messages.append({"role": "user", "content": results})
        return {"final_text": final_text, "stop": stop, "steps": steps, "usage": usage.to_dict(),
                "seconds": round(time.time() - started, 1)}


# ---------------------------------------------------------------- OpenAI-compatible

class OpenAIClient:
    def __init__(self, model, api_key, base_url, effort, max_tokens, price_in, price_out):
        import openai
        self.openai = openai
        self.client = openai.OpenAI(api_key=api_key, base_url=base_url, max_retries=4, timeout=900.0)
        self.model, self.effort, self.max_tokens = model, effort, max_tokens
        self.price_in, self.price_out = price_in, price_out

    def _call(self, messages, usage, tools=None):
        o = self.openai
        p = {"model": self.model, "messages": messages, "max_completion_tokens": self.max_tokens}
        if self.effort:
            p["reasoning_effort"] = self.effort
        if tools:
            p["tools"] = [{"type": "function", "function": {
                "name": t["name"], "description": t["description"], "parameters": t["schema"]}} for t in tools]
        try:
            # Streamed, so that slow answers keep bytes flowing and gateways in
            # front of the endpoint do not time the request out (HTTP 504).
            with self.client.chat.completions.stream(**p, stream_options={"include_usage": True}) as stream:
                resp = stream.get_final_completion()
        except o.AuthenticationError as e:
            raise ProviderError(f"authentication failed: {e.message}") from e
        except o.BadRequestError as e:
            raise ProviderError(f"bad request: {e.message}") from e
        except o.APIStatusError as e:
            raise ProviderError(f"API error {e.status_code}: {e.message}") from e
        except o.APIConnectionError as e:
            raise ProviderError(f"connection error: {e}") from e
        u = resp.usage
        if u:
            details = getattr(u, "prompt_tokens_details", None)
            cached = (getattr(details, "cached_tokens", 0) or 0) if details else 0
            usage.add((u.prompt_tokens or 0) - cached, u.completion_tokens or 0, cached, 0)
        else:
            usage.add()
        return resp

    def oneshot(self, system, prompt):
        usage = Usage(self.model, self.price_in, self.price_out)
        resp = self._call([{"role": "system", "content": system}, {"role": "user", "content": prompt}], usage)
        choice = resp.choices[0]
        return {"text": choice.message.content or "", "stop_reason": choice.finish_reason,
                "usage": usage.to_dict(), "raw": resp.model_dump()}

    def agent(self, system, prompt, tools, execute, limits, log):
        usage = Usage(self.model, self.price_in, self.price_out)
        messages = [{"role": "system", "content": system}, {"role": "user", "content": prompt}]
        log({"type": "user", "content": prompt})
        started, steps, final_text, stop = time.time(), 0, "", None
        while True:
            stop = _stop_reason_for(limits, steps, usage, started)
            if stop:
                break
            resp = self._call(messages, usage, tools)
            steps += 1
            choice = resp.choices[0]
            m = choice.message
            log({"type": "assistant", "step": steps, "message": m.model_dump(), "usage_so_far": usage.to_dict()})
            entry = {"role": "assistant", "content": m.content or ""}
            if m.tool_calls:
                entry["tool_calls"] = [{"id": c.id, "type": "function", "function": {
                    "name": c.function.name, "arguments": c.function.arguments}} for c in m.tool_calls]
            messages.append(entry)
            final_text = m.content or final_text
            if not m.tool_calls:
                stop = "end_turn" if choice.finish_reason != "content_filter" else "refusal"
                break
            for c in m.tool_calls:
                try:
                    args = json.loads(c.function.arguments or "{}")
                    out, is_error = execute(c.function.name, args)
                except json.JSONDecodeError:
                    args, out, is_error = c.function.arguments, "error: tool arguments were not valid JSON", True
                log({"type": "tool_result", "tool": c.function.name, "input": args, "output": out, "is_error": is_error})
                messages.append({"role": "tool", "tool_call_id": c.id, "content": out})
        return {"final_text": final_text, "stop": stop, "steps": steps, "usage": usage.to_dict(),
                "seconds": round(time.time() - started, 1)}


# ---------------------------------------------------------------- self-test

class ScriptedClient:
    """No network: plays back a fixed list of tool calls. Used by --provider scripted
    to test the agent loop, tools and grading end to end."""

    def __init__(self, script, final_text="done"):
        self.script, self.final_text, self.model = script, final_text, "scripted"

    def oneshot(self, system, prompt):
        raise ProviderError("the scripted provider supports agent mode only")

    def agent(self, system, prompt, tools, execute, limits, log):
        usage = Usage("scripted")
        log({"type": "user", "content": prompt})
        for i, (name, args) in enumerate(self.script, 1):
            usage.add()
            log({"type": "assistant", "step": i, "message": {"tool": name, "input": args}})
            out, is_error = execute(name, args)
            log({"type": "tool_result", "tool": name, "input": args, "output": out, "is_error": is_error})
        return {"final_text": self.final_text, "stop": "end_turn", "steps": len(self.script),
                "usage": usage.to_dict(), "seconds": 0.0}
