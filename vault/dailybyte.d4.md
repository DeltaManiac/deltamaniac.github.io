---
id: 98c5YzqkL91Qg2fN3vRow
title: Capitalized Properly ??
desc: ''
updated: 1628434950340
created: 1628212076920
nav_order: 4
---

# Problem

This question is asked by Google.

Given a string, return whether or not it uses capitalization correctly. A string correctly uses capitalization if all letters are capitalized, no letters are capitalized, or only the first letter is capitalized.

Ex: Given the following strings...

> "USA", return true
>
> "Calvin", return true
>
> "compUter", return false
>
> "coding", return true


## [[python]]
```python
def check(word:str)->bool:
    if word.isupper():
        return True
    if word.islower():
        return True
    if word[0].isupper() and word[1:].islower():
        return True
    return False
```

## [[go]]
```go
func check(word string) bool {
	if isUpper(word) {
		return true
	}
	if isLower(word) {
		return true
	}
	if isUpper(word[:1]) && isLower(word[1:]) {
		return true
	}
	return false
}

func isUpper(word string) bool {
	for _, c := range word {
		if !unicode.IsUpper(c) {
			return false
		}
	}
	return true
}

func isLower(word string) bool {
	for _, c := range word {
		if !unicode.IsLower(c) {
			return false
		}
	}
	return true
}
```
## [[rust]]

