# Justified text

The first line of standard input holds the line width `W` (between 10 and
60). The rest of the input is text: its words are the runs of characters
other than spaces, read across all the remaining lines in order. No word is
longer than `W`.

Fill output lines greedily: each line takes as many of the next words as fit
in `W` characters with one space between neighboring words. Then print every
line:

- The last line: its words with one space between them, and nothing after
  the last word.
- Any other line with one word: that word alone.
- Any other line: exactly `W` characters, starting with its first word and
  ending with its last word. The spaces between words are spread as evenly as
  possible; when they do not divide evenly, the gaps further left get one
  more space than the gaps further right.

If there are no words, print nothing.

Write a {{.Lang}} program that does this. For example, with width 16 the
text `This is an example of text justification.` gives:

```
This    is    an
example  of text
justification.
```
