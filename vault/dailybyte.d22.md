---
id: H8MXI19M4LJ0SbFIX5H36
title: Balanced Brackets
desc: ''
updated: 1629868101060
created: 1629698682065
nav_order: 22
---
# Problem

This question is asked by Google.

Given a string only containing the following characters `(`, `)`, `{`, `}`, `[`, and `]` return whether or not the opening and closing characters are in a valid order.

Ex: Given the following strings...

>"(){}[]", return true
>
>"(({[]}))", return true
>
>"{(})", return false

## [[python]]

```python
def check_brackets(a):
    stk = []
    chars = { "{":"}","[":"]","(":")"}
    for x in a:
        if x in chars.keys():
            stk.append(x)
        if x in chars.values():
            if x== chars.get(stk[-1]):
                stk.pop()
            else:
                return False

    return len(stk) == 0
```

## [[go]]

## [[rust]]