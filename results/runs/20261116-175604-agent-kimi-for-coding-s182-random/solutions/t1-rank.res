tosedo slice(s, start, count)
    sheye out <- "";
    sho (sheye i <- 0; i < count; i <- i + 1) {
        out <- out + s[start + i];
    }
    cha out;
bawoum tosedo

tosedo lowerBound(xs, x)
    sheye lo <- 0;
    sheye hi <- louwo(xs);
    veshim (lo < hi) {
        sheye mid <- (lo + hi) / 2;
        wesosa (xs[mid] < x) {
            lo <- mid + 1;
        } oli {
            hi <- mid;
        }
    }
    cha lo;
bawoum tosedo

tosedo parseNums(first, nums)
    sheye i <- 0;
    sheye n <- louwo(first);
    veshim (i < n) {
        wesosa (first[i] = " ") {
            i <- i + 1;
        } oli {
            sheye j <- i;
            sheye goon <- j < n;
            veshim (goon) {
                wesosa (first[j] = " ") {
                    goon <- ishe;
                } oli {
                    j <- j + 1;
                    goon <- j < n;
                }
            }
            omse(nums, odresdra(slice(first, i, j - i)));
            i <- j + 1;
        }
    }
    cha 0;
bawoum tosedo

sheye first <- diwela();
sheye nums <- [];
wesosa (first <> malwe) {
    parseNums(first, nums);
}
sheye line <- diwela();
veshim (line <> malwe) {
    sheye x <- odresdra(line);
    sheye cnt <- 0;
    sheye found <- ishe;
    wesosa (louwo(nums) > 0) {
        cnt <- lowerBound(nums, x);
        wesosa (cnt < louwo(nums)) {
            wesosa (nums[cnt] = x) {
                found <- shilsa;
            }
        }
    }
    wesosa (found) {
        wami cnt + " found";
    } oli {
        wami cnt + " missing";
    }
    line <- diwela();
}
