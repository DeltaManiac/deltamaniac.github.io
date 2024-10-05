+++
title = "TIS-100 Segment : 51781"
date = "2022-11-12T22:47:59.366000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Image Test Pattern 2

### Solution

![](/images/games/tis-100/segment/51781/1.png) 

### Solution

```
@0

@1

@2

@3

@4

@5

@6

@7

@8

@9

@10
ST: MOV ACC,DOWN
SWP
MOV ACC DOWN
MOV 3,DOWN
MOV -1,DOWN
SWP
SUB 27
JGZ NX
ADD 29
JMP ST

NX: SUB,2
SWP
ADD 1
SWP

@11

```