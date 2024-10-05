+++
title = "TIS-100 Segment : 40196"
date = "2022-11-12T21:53:29.807000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Signal Pattern Detector

### Solution

![](/images/games/tis-100/segment/40196/1.png)


### Solution

```
@0

@1
0:
MOV ANY,ACC
MOV 0 ANY
JNZ 0
1:
MOV ANY,ACC
MOV 0,ANY
JNZ 0
2:
MOV ANY,ACC
JNZ RESET
MOV 1,ANY
JMP 2
RESET:
MOV 0,ANY

@2
MOV LEFT,DOWN

@3

@4

@5

@6
MOV UP,DOWN

@7

@8

@9

@10
MOV UP,DOWN

@11

```