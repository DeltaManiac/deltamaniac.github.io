## Problem

This question is asked by Amazon.

Given two strings s and t, which represents a sequence of keystrokes, where # denotes a backspace, return whether or not the sequences produce the same result.

Ex: Given the following strings...

<pre>
s = "ABC#", t = "CD##AB", return true

s = "como#pur#ter", t = "computer", return true

s = "cof#dim#ng", t = "code", return false
</pre>

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

