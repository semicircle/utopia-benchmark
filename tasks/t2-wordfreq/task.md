# Word frequencies

Standard input contains zero or more lines of text (printable ASCII
characters). A word is a maximal run of letters `A`–`Z` and `a`–`z`; every
other character separates words. Upper and lower case count as the same
letter.

Write a {{.Lang}} program that counts how often each word occurs and prints
the ten most frequent words, one per line, as the word in lower case, a
space, and its count. Order them by count, highest first, and words with the
same count alphabetically. If there are fewer than ten distinct words, print
them all.

For example, the input `The cat and THE hat.` gives:

```
the 2
and 1
cat 1
hat 1
```
