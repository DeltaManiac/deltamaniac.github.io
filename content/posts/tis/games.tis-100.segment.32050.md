+++
title = "TIS-100 Segment : 32050"
date = "2022-11-12T21:04:15.212000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Signal Edge Detector

### Solution

![](/images/games/tis-100/segment/32050/1.png)

### Solution

```
@0

@1
MOV UP ACC
MOV ACC RIGHT
MOV ACC RIGHT

@2
SUB LEFT
JLZ NEG
JMP SIG
NEG:
NEG
SIG:
MOV ACC,DOWN
MOV LEFT, ACC

@3

@4

@5

@6
START:
MOV UP,ACC
SUB 10
JLZ SIG0
SIG1:
MOV 1,DOWN
JMP START

SIG0:
MOV 0,DOWN

@7

@8

@9 

@10
MOV UP, DOWN

@11

```