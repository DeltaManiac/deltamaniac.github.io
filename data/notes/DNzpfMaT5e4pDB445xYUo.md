
# Problem

This question is asked by Amazon. Given a string s consisting of only letters and digits, where we are allowed to transform any letter to uppercase or lowercase, return a list containing all possible permutations of the string.

Ex: Given the following string…
```
S = "c7w2", return ["c7w2", "c7W2", "C7w2", "C7W2"]
```

## [[python]]

```python
def letterCasePermutation(self, S):
    def backtrack(sub="", i=0):
        if len(sub) == len(S):
            res.append(sub)
        else:
            if S[i].isalpha():
                backtrack(sub + S[i].swapcase(), i + 1)
            backtrack(sub + S[i], i + 1)

    res = []
    backtrack()
    return res
``
## [[go]]

## [[rust]]

