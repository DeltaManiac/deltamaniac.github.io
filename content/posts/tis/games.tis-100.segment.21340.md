+++
title = "TIS-100 Segment : 21340"
date = "2020-11-05T21:21:53.725000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Signal Comparator

### Solution

![](/images/games/tis-100/segment/21340/1.png)

### Solution

```
@0
MOV UP,DOWN

@1


@2


@3


@4
MOV UP,DOWN

@5
MOV UP,RIGHT

@6
START:
MOV LEFT,ACC
JGZ WRITE1
MOV ACC,RIGHT
MOV 0,DOWN
JMP START


WRITE1:
MOV ACC,RIGHT
MOV 1,DOWN
JMP START

@7
START:
MOV LEFT,ACC
JEZ WRITE1
MOV ACC,RIGHT
MOV 0,DOWN
JMP START


WRITE1:
MOV ACC,RIGHT
MOV 1,DOWN
JMP START

@8
START:
MOV LEFT,ACC
JLZ WRITE1
MOV 0,DOWN
JMP START


WRITE1:
MOV 1,DOWN
JMP START


@9

@10

@11

```