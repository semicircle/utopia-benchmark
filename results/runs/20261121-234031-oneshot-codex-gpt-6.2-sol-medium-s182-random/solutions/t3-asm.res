tosedo fields(line)
    sheye result <- [];
    sheye token <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (line[i] = " ") {
            omse(result, token);
            token <- "";
        } oli {
            token <- token + line[i];
        }
    }
    omse(result, token);
    cha result;
bawoum tosedo

tosedo operand(token, letters)
    sheye first <- token[0];
    wesosa ((first >= "a") dilisyo (first <= "z")) {
        sheye i <- 0;
        veshim (letters[i] <> first) {
            i <- i + 1;
        }
        cha [i, 0];
    }
    cha [-1, odresdra(token)];
bawoum tosedo

tosedo readOperand(arg, registers)
    sheye i <- arg[0];
    wesosa (i = -1) {
        cha arg[1];
    }
    cha registers[i];
bawoum tosedo

tosedo quotient(a, b)
    sheye q <- a / b;
    wesosa (((a < 0) <> (b < 0)) dilisyo ((a drossou b) <> 0)) {
        q <- q + 1;
    }
    cha q;
bawoum tosedo

sheye letters <- "abcdefghijklmnopqrstuvwxyz";
sheye program <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye parts <- fields(line);
    sheye instruction <- [parts[0], operand(parts[1], letters)];
    wesosa (louwo(parts) = 3) {
        omse(instruction, operand(parts[2], letters));
    }
    omse(program, instruction);
    line <- diwela();
}

sheye registers <- [];
sho (sheye i <- 0; i < 26; i <- i + 1) {
    omse(registers, 0);
}
sheye pc <- 0;
sheye executed <- 0;
sheye length <- louwo(program);
veshim ((pc >= 0) dilisyo (pc < length)) {
    wesosa (executed = 10000) {
        wami "timeout";
        cha;
    }
    executed <- executed + 1;
    sheye instruction <- program[pc];
    sheye op <- instruction[0];
    sheye first <- instruction[1];
    sheye next <- pc + 1;
    wesosa (op = "out") {
        wami readOperand(first, registers);
    } oli wesosa (op = "jnz") {
        wesosa (readOperand(first, registers) <> 0) {
            next <- pc + readOperand(instruction[2], registers);
        }
    } oli {
        sheye r <- first[0];
        sheye a <- registers[r];
        sheye b <- readOperand(instruction[2], registers);
        moumare amdre op
        amdre "set"
            registers[r] <- b;
        amdre "add"
            registers[r] <- a + b;
        amdre "sub"
            registers[r] <- a - b;
        amdre "mul"
            registers[r] <- a * b;
        amdre "div", "mod"
            wesosa (b = 0) {
                wami "error";
                cha;
            }
            sheye q <- quotient(a, b);
            wesosa (op = "div") {
                registers[r] <- q;
            } oli {
                registers[r] <- a - (b * q);
            }
        bawoum moumare
    }
    pc <- next;
}
