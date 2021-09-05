---
id: yN60NwY48svexBLDole4V
title: Sum Digits Until One
desc: ''
updated: 1630819598654
created: 1630601718305
nav_order: 11
---

## Problem

We're provided a positive integer num. Can you write a method to repeatedly add all of its digits until the result has only one digit?

Here's an example: if the input was 49, we'd go through the following steps:

> // start with 49
> 4 + 9 = 13
>
> // move onto 13
> 1 + 3 = 4

We would then return 4.

Constraints

    Input will be in the range between 0 and 1000000000
    Expected time complexity : O(log n)
    Expected space complexity : O(1)



## [[python]]

```python
def sumTillOne(n):
    new = n
    while new>9:
        sum = 0
        while new > 9:
           sum = sum + new % 10
           new = new // 10
        sum = sum + new
        new = sum
    return new
```