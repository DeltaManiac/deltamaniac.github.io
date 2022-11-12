---
id: qvsve4bcorl4qxchnfiuusf
title: '42656'
desc: ''
updated: 1668272467397
created: 1668271841497
---
## Sequence Reverser

# Solution

```
@0

@1
MOV UP,DOWN

@2

@3

@4

@5
MOV UP,RIGHT

@6
MOV 0,UP

FORWARD: 
MOV LEFT,ACC
MOV ACC,UP
JGZ FORWARD
MOV UP,NIL

REVERSE: 
MOV UP,ACC
MOV ACC,DOWN
JGZ REVERSE

@7

@8

@9

@10
MOV UP,DOWN

@11

```

# Solution

![](/assets/images/2022-11-12-22-21-37.png)
