---
id: eN5kq8a6uewxD6Lgvlj9V
title: Day 5
desc: ''
updated: 1628397573181
created: 1628394332314
nav_order: 5
---
# Problem
This question is asked by Apple. Given two binary strings (strings containing only 1s and 0s) return their sum (also as a binary string).
Note: neither binary string will contain leading 0s unless the string itself is 0

Ex: Given the following binary strings...

> "100" + "1", return "101"
> "11" + "1", return "100"
> "1" + "0", return  "1"

## [[python]]
```python
def add(num1:str, num2:str)->str:
    return bin(int(num1,2)+int(num2,2))[2:]
```
## [[go]]

## [[rust]]
