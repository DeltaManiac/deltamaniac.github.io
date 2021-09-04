---
id: ohFCtqpYV2G0Z6JgQ6Yct
title: Reverse String
desc: ''
updated: 1629045487923
created: 1627950805305
nav_order: 1
---

# Problem

This question is asked by Google.

Given a string, reverse all of its characters and return the resulting string.

Ex: Given the following strings...

> "Cat", return "taC"
>
> "The Daily Byte", return "etyB yliaD ehT"
>
> "civic", return "civic"

## [[python]]

```python
def reverse(word)
    return word[::-1]
```

## [[go]]

```go
func reverse(s string) string {
    // Handle UTF-16
    rns := []rune(s)
    for i, j := 0, len(rns)-1; i < j; i, j = i+1, j-1 {
        rns[i], rns[j] = rns[j], rns[i]
    }
    return string(rns)
}
```

## [[rust]]
```rust
// Handle UTF-16
use unicode_segementation:UnicodeSegmentation;
fn reverse(word:&str)-> String{
    word
        .graphemes(true)
        .rev()
        .flat_map(|g| g.chars())
        .collect()
}
```
