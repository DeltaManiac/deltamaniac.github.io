+++
title = "TIS-100 Segment : 22280"
date = "2020-11-05T21:24:52.143000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Signal Multiplexer

### Solution

![](/images/games/tis-100/segment/22280/1.png)

### Solution

```
@0


@1
MOV UP,DOWN

@2
MOV UP,DOWN

@3
MOV UP,DOWN

@4


@5
MOV UP,RIGHT

@6
START:
MOV UP,ACC
JEZ READ_BOTH
JGZ READ_RIGHT
MOV RIGHT,ACC
MOV LEFT,DOWN
JMP START
READ_RIGHT:
MOV LEFT,ACC
MOV RIGHT,DOWN
JMP START
READ_BOTH:
MOV RIGHT,ACC
ADD LEFT
MOV ACC,DOWN

@7
MOV UP,LEFT

@8


@9
MOV UP,DOWN

@10

@11

```