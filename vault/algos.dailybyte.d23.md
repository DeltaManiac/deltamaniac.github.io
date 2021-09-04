---
id: INDH1D7my74PgGKOjkDop
title: Compare Keystrokes
desc: ''
updated: 1629874570833
created: 1629873991703
nav_order: 23
---
## Problem

This question is asked by Amazon.

Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

> s = "ABC#", t = "CD##AB", return true
>
> s = "como#pur#ter", t = "computer", return true
>
> s = "cof#dim#ng", t = "code", return false

## [[python]]

```python
def compare_keystrokes(s1,s2) -> bool:
    stk = []
    stk2 = []
    for x in s1:
        if x == '#':
            stk.pop()
        else:
            stk.append(x)
    for x in s2:
        if x == '#':
            stk2.pop()
        else:
            stk2.append(x)
    return stk==stk2
```

## [[go]]

## [[rust]]

