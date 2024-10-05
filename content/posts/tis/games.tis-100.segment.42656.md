+++
title = "TIS-100 Segment : 42656"
date = "2022-11-12T22:20:41.497000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Sequence Reverser

### Solution

![](/images/games/tis-100/segment/42656/1.png) 

### Solution

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