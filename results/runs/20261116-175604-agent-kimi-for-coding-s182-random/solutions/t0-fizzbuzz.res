sheye n <- odresdra(diwela());
sho (sheye i <- 1; i <= n; i <- i + 1) {
    sheye d3 <- (i drossou 3) = 0;
    sheye d5 <- (i drossou 5) = 0;
    wesosa (d3 dilisyo d5) {
        wesosa (d3 dilisyo (drol d5)) {
            wami "Fizz";
        } oli wesosa ((drol d3) dilisyo d5) {
            wami "Buzz";
        } oli {
            wami "FizzBuzz";
        }
    } oli {
        wami i;
    }
}
