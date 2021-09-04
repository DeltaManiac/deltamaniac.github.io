---
id: XM1Z7OUbeItoYxJICWxeN
title: Will It Return ??
desc: ''
updated: 1628434941643
created: 1628100232230
nav_order: 3
---

# Problem

This question is asked by Amazon.

 Given a string representing the sequence of moves a robot vacuum makes, return whether or not it will return to its original position. The string will only contain L, R, U, and D characters, representing left, right, up, and down respectively.

Ex: Given the following strings...

> "LR", return true
>
> "URURD", return false
>
> "RUULLDRD", return true

## [[python]]
```python
def does_it_return(word)->bool:
    x,y = 0,0
    for c in word:
        if c == 'R':
            x+=1
        elif c == 'L':
            x-=1
        elif c == 'U':
            y += 1
        elif c == 'D':
            y-=1
    return x==0 and y==0
```

## [[go]]
```go
func doesitreturn(word string) bool {
	x := 0
	y := 00
	for _, c := range word {
		if c == 'R' {
			x = x + 1
		} else if c == 'L' {
			x = x - 1
		} else if c == 'U' {
			y += 1
		} else if c == 'D' {
			y -= 1
		}
	}
	return x == 0 && y == 0
}
```

## [[rust]]

```rust
fn does_it_return(word:&str)->bool{
    let mut x = 0;
    let mut y = 0;

    for c in word.chars() {
        if c == 'R' {
            x += 1;
        } else if c == 'L' {
            x -= 1;
        } else if c == 'U' {
            y += 1;
        } else {
            y -= 1;
        }
    }
    x == 0 && y == 0
}

}
```
