sheye evenCount <- 0;
sheye oddCount <- 0;
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n drossou 2) = 0) {
        evenCount <- evenCount + 1;
    } oli {
        oddCount <- oddCount + 1;
    }
    line <- diwela();
}
wami "even " + evenCount;
wami "odd " + oddCount;
