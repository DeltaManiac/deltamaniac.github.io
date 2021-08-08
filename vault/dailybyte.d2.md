---
id: 8CvV1rkawfYZGgMX
title: Day 2
desc: ''
updated: 1628394312627
created: 1628005470068
nav_order: 2
---


 # Problem

This question is asked by Facebook. Given a string, return whether or not it forms a palindrome ignoring case and non-alphabetical characters.
Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

> "level", return true
> "algorithm", return false
> "A man, a plan, a canal: Panama.", return true

 ## [[python]]

```python
def is_palindrome(word)->bool:
    w1 = "".join(list(filter(lambda x: x.isalpha(),word.lower())))
    return w1==w1[::-1]
```

 ## [[go]]

```go
func isPalindrome(word string) bool{
    s := strings.ToLower(word)
    i, j := 0, len(s)-1
    for i < j {
        if !isValid(s[i]) {
            i++
            continue
        }
        if !isValid(s[j]) {
            j--
            continue
        }
        if !strings.EqualFold(string(s[i]), string(s[j])) {
            return false
        }
        i++
        j--
    }
    return true
}

func isValid(a byte) bool {
    if (a >= 'a' && a <= 'z') {
        return true
    }
    return false
}
}
```

 ## [[rust]]

```rust
fn isPalindrome(word:&str)-> bool{
    extern crate unicode_segmentation;
    use unicode_segmentation::UnicodeSegmentation;
    word == word
        .graphemes(true)
        .rev()
        .flat_map(|g| g.chars())
        .collect::<String>()
}

```