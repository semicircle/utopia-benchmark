wami ("0" >= "0") dilisyo ("0" <= "9");
wami ("9" >= "0") dilisyo ("9" <= "9");
wami ("/" >= "0") dilisyo ("/" <= "9");
wami (":" >= "0") dilisyo (":" <= "9");
sheye a <- [1, 2];
sheye b <- a;
a[0] <- 9;
wami b;
