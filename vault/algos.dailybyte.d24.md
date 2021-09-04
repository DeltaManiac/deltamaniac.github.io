---
id: NrfqZ1XT6IxUMfJcr15O7
title: Remove Adjacent Chars
desc: ''
updated: 1629874696155
created: 1629874608161
nav_order: 24
---

# Problem

This question is asked by Facebook.

Given a string s containing only lowercase letters, continuously remove adjacent characters that are the same and return the result.

Ex: Given the following strings...


>s = "abccba", return ""
>
>s = "foobar", return "fbar"
>
>s = "abccbefggfe", return "a"

## [[python]]

```python
def remove_adjacent(s1):
    stk = []
    for x in s1:
        if len(stk)>0 and stk[-1] == x:
            stk.pop()
        else:
            stk.append(x)

    return "".join(stk)
```

## [[go]]

## [[rust]]

