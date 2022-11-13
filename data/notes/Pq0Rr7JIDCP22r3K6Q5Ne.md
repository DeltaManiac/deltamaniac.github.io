## Problem

This question is asked by Facebook.

Given a string and the ability to delete at most one character, return whether or not it can form a palindrome.

Note: a palindrome is a sequence of characters that reads the same forwards and backwards.

Ex: Given the following strings...

> "abcba", return true
>
> "foobof", return true (remove the first 'o', the second 'o', or 'b')
>
> "abccab", return false

## [[python]]

```python
def validPalindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if s[left] != s[right]:
            one, two = s[left:right], s[left + 1:right + 1]
            return one == one[::-1] or two == two[::-1]
        left, right = left + 1, right - 1
    return True
```

## [[go]]

## [[rust]]

