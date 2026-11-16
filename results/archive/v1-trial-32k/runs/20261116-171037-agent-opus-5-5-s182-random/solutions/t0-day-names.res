sheye names <- ["invalid", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"];
sheye line <- diwela();
veshim (line <> malwe) {
    sheye n <- odresdra(line);
    wesosa ((n >= 1) dilisyo (n <= 7)) {
        wami names[n];
    } oli {
        wami "invalid";
    }
    line <- diwela();
}
