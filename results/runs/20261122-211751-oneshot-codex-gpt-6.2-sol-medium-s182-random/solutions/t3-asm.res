tosedo split(line)
    sheye words <- [];
    sheye token <- "";
    sho (sheye i <- 0; i < louwo(line); i <- i + 1) {
        wesosa (line[i] = " ") {
            omse(words, token);
            token <- "";
        } oli {
            token <- token + line[i];
        }
    }
    omse(words, token);
    cha words;
bawoum tosedo

tosedo operand(token)
    wesosa ((louwo(token) = 1) dilisyo ((token >= "a") dilisyo (token <= "z"))) {
        sheye alphabet <- "abcdefghijklmnopqrstuvwxyz";
        sheye index <- 0;
        veshim (alphabet[index] <> token) {
            index <- index + 1;
        }
        cha [shilsa, index];
    }
    cha [ishe, odresdra(token)];
bawoum tosedo

tosedo value(arg, registers)
    wesosa (arg[0]) {
        cha registers[arg[1]];
    }
    cha arg[1];
bawoum tosedo

sheye program <- [];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye words <- split(line);
    sheye second <- malwe;
    wesosa (louwo(words) = 3) {
        second <- operand(words[2]);
    }
    omse(program, [words[0], operand(words[1]), second]);
    line <- diwela();
}

sheye registers <- [];
sho (sheye i <- 0; i < 26; i <- i + 1) {
    omse(registers, 0);
}
sheye pc <- 0;
sheye executed <- 0;
veshim ((pc >= 0) dilisyo (pc < louwo(program))) {
    wesosa (executed = 10000) {
        wami "timeout";
        cha;
    }
    executed <- executed + 1;
    sheye instruction <- program[pc];
    sheye op <- instruction[0];
    sheye first <- instruction[1];
    moumare amdre op
    amdre "out"
        wami value(first, registers);
    amdre "jnz"
        wesosa (value(first, registers) <> 0) {
            pc <- pc + value(instruction[2], registers);
            chidrom;
        }
    amdre oli
        sheye index <- first[1];
        sheye a <- registers[index];
        sheye b <- value(instruction[2], registers);
        moumare amdre op
        amdre "set"
            registers[index] <- b;
        amdre "add"
            registers[index] <- a + b;
        amdre "sub"
            registers[index] <- a - b;
        amdre "mul"
            registers[index] <- a * b;
        amdre "div", "mod"
            wesosa (b = 0) {
                wami "error";
                cha;
            }
            sheye q <- a / b;
            wesosa ((q < 0) dilisyo ((a drossou b) <> 0)) {
                q <- q + 1;
            }
            wesosa (op = "div") {
                registers[index] <- q;
            } oli {
                registers[index] <- a - (b * q);
            }
        bawoum moumare
    bawoum moumare
    pc <- pc + 1;
}
