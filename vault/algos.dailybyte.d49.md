---
id: l66OlsoH7P9OOtSgFeAqO
title: Generate Search Message
desc: ''
updated: 1633168894583
created: 1633151914918
nav_order: 49
---

# Problem

This question is asked by Google.

Given a string of digits, return all possible text messages those digits could send.

Note: The mapping of digits to letters is as follows…
```
0 -> null
1 -> null
2 -> "abc"
3 -> "def"
4 -> "ghi"
5 -> "jkl"
6 -> "mno"
7 -> "pqrs"
8 -> "tuv"
9 -> "wxyz"
```

```
Ex: digits = "23" return ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
```

## [[python]]

```python
def generateMessage(digits):
    chars_map = { 2: "abc", 3:"def", 4:"ghi", 5:"jkl", 6:"mno", 7:"pqrs", 8:"tuv", 9:"wxyz"}
    message = []
    for c in digits:
        digit = int(c)
        chars = chars_map.get(digit)
        if chars is None:
            continue
        if len(message) == 0:
            message = list(chars)
        else:
            perms = [ head + char for head in perms for char in chars]
    return perms
```

## [[go]]

## [[rust]]
