---
id: aD28cj9vhLvlrp0y3mO6P
title: Day 9
desc: ''
updated: 1628435025844
created: 1628431635440
nav_order: 9
---

# Problem
This question is asked by Amazon.
Given a string representing your stones and another string representing a list of jewels, return the number of stones that you have that are also jewels.

Ex: Given the following jewels and stones...

> jewels = "abc", stones = "ac", return 2
>
> jewels = "Af", stones = "AaaddfFf", return 3
>
> jewels = "AYOPD", stones = "ayopd", return 0

## [[python]]

```python
def is_jewel_and_stone(jewels,stones):
    return len(set(jewels).intersection(set(stones)))
```

## [[go]]

## [[rust]]