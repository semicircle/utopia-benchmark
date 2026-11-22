tosedo divz(a, b)
    sheye q <- a / b;
    sheye r <- a - b * q;
    wesosa (r <> 0) {
        wesosa ((r < 0) <> a < 0) {
            wesosa ((r < 0) = b < 0) {
                q <- q + 1;
            } oli {
                q <- q - 1;
            }
        }
    }
    cha q;
bawoum tosedo

tosedo modz(a, b)
    cha a - b * divz(a, b);
bawoum tosedo

wami divz(-7, 2);
wami modz(-7, 2);
wami divz(7, -2);
wami modz(7, -2);
wami divz(-7, -2);
wami modz(-7, -2);
wami divz(7, 2);
wami modz(7, 2);
wami divz(-8, 3);
wami modz(-8, 3);
wami divz(8, -3);
wami modz(8, -3);
wami divz(0, 5);
wami modz(0, -5);
wami divz(5, 1);
wami divz(-5, 1);
wami divz(5, -1);
wami divz(-5, -1);

' string concat grouping
wami ("x" + 1) + 2;
wami (("a" + "b") + "c");

sheye line <- diwela();
wami line;
sheye line2 <- diwela();
wami line2;
