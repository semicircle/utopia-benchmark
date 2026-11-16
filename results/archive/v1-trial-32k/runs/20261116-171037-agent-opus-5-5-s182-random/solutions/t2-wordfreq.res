tosedo lowIdx(c)
    wesosa (c < "n") {
        wesosa (c < "g") {
            wesosa (c < "d") {
                wesosa (c < "b") {
                    cha 0;
                }
                wesosa (c < "c") {
                    cha 1;
                }
                cha 2;
            }
            wesosa (c < "e") {
                cha 3;
            }
            wesosa (c < "f") {
                cha 4;
            }
            cha 5;
        }
        wesosa (c < "j") {
            wesosa (c < "h") {
                cha 6;
            }
            wesosa (c < "i") {
                cha 7;
            }
            cha 8;
        }
        wesosa (c < "l") {
            wesosa (c < "k") {
                cha 9;
            }
            cha 10;
        }
        wesosa (c < "m") {
            cha 11;
        }
        cha 12;
    }
    wesosa (c < "t") {
        wesosa (c < "q") {
            wesosa (c < "o") {
                cha 13;
            }
            wesosa (c < "p") {
                cha 14;
            }
            cha 15;
        }
        wesosa (c < "r") {
            cha 16;
        }
        wesosa (c < "s") {
            cha 17;
        }
        cha 18;
    }
    wesosa (c < "w") {
        wesosa (c < "u") {
            cha 19;
        }
        wesosa (c < "v") {
            cha 20;
        }
        cha 21;
    }
    wesosa (c < "y") {
        wesosa (c < "x") {
            cha 22;
        }
        cha 23;
    }
    wesosa (c < "z") {
        cha 24;
    }
    cha 25;
bawoum tosedo

tosedo upIdx(c)
    wesosa (c < "N") {
        wesosa (c < "G") {
            wesosa (c < "D") {
                wesosa (c < "B") {
                    cha 0;
                }
                wesosa (c < "C") {
                    cha 1;
                }
                cha 2;
            }
            wesosa (c < "E") {
                cha 3;
            }
            wesosa (c < "F") {
                cha 4;
            }
            cha 5;
        }
        wesosa (c < "J") {
            wesosa (c < "H") {
                cha 6;
            }
            wesosa (c < "I") {
                cha 7;
            }
            cha 8;
        }
        wesosa (c < "L") {
            wesosa (c < "K") {
                cha 9;
            }
            cha 10;
        }
        wesosa (c < "M") {
            cha 11;
        }
        cha 12;
    }
    wesosa (c < "T") {
        wesosa (c < "Q") {
            wesosa (c < "O") {
                cha 13;
            }
            wesosa (c < "P") {
                cha 14;
            }
            cha 15;
        }
        wesosa (c < "R") {
            cha 16;
        }
        wesosa (c < "S") {
            cha 17;
        }
        cha 18;
    }
    wesosa (c < "W") {
        wesosa (c < "U") {
            cha 19;
        }
        wesosa (c < "V") {
            cha 20;
        }
        cha 21;
    }
    wesosa (c < "Y") {
        wesosa (c < "X") {
            cha 22;
        }
        cha 23;
    }
    wesosa (c < "Z") {
        cha 24;
    }
    cha 25;
bawoum tosedo

sheye UP <- "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
sheye LO <- "abcdefghijklmnopqrstuvwxyz";
sheye NB <- 4096;
sheye buckets <- [];
sho (sheye i <- 0; i < NB; i <- i + 1) {
    omse(buckets, []);
}
sheye entries <- [];

tosedo addWord(buckets, entries, w, h)
    sheye b <- buckets[h];
    sho (sheye i <- 0; i < louwo(b); i <- i + 1) {
        sheye e <- b[i];
        wesosa (e[0] = w) {
            e[1] <- e[1] + 1;
            cha;
        }
    }
    sheye ne <- [w, 1];
    omse(b, ne);
    omse(entries, ne);
bawoum tosedo

sheye line <- diwela();
veshim (line <> malwe) {
    sheye cur <- "";
    sheye h <- 0;
    sheye n <- louwo(line);
    sho (sheye i <- 0; i < n; i <- i + 1) {
        sheye c <- line[i];
        wesosa (c >= "a") {
            wesosa (c <= "z") {
                cur <- cur + c;
                h <- ((h * 31) + lowIdx(c)) drossou NB;
                chidrom;
            }
        } oli wesosa (c >= "A") {
            wesosa (c <= "Z") {
                sheye k <- upIdx(c);
                cur <- cur + LO[k];
                h <- ((h * 31) + k) drossou NB;
                chidrom;
            }
        }
        wesosa (cur <> "") {
            addWord(buckets, entries, cur, h);
            cur <- "";
            h <- 0;
        }
    }
    wesosa (cur <> "") {
        addWord(buckets, entries, cur, h);
    }
    line <- diwela();
}

' selection of top 10
sheye m <- louwo(entries);
sheye used <- [];
sho (sheye i <- 0; i < m; i <- i + 1) {
    omse(used, ishe);
}
sho (sheye r <- 0; (r < 10) dilisyo (r < m); r <- r + 1) {
    sheye best <- -1;
    sho (sheye i <- 0; i < m; i <- i + 1) {
        wesosa (drol used[i]) {
            wesosa (best < 0) {
                best <- i;
            } oli {
                sheye e <- entries[i];
                sheye f <- entries[best];
                wesosa (e[1] > f[1]) {
                    best <- i;
                } oli wesosa ((e[1] = f[1]) dilisyo (e[0] < f[0])) {
                    best <- i;
                }
            }
        }
    }
    used[best] <- shilsa;
    sheye eb <- entries[best];
    wami (eb[0] + " ") + eb[1];
}
