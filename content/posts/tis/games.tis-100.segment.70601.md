+++
title = "TIS-100 Segment : 70601"
date = "2022-11-13T10:42:38.460000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Stored Image Decoder

### Solution

![](/images/games/tis-100/segment/70601/1.png) 


### Solution

```
@0

@1
 MOV UP ACC
 SWP # COLOR
 MOV UP ACC
 SWP # LENGTH
LOOP: SWP # COLOR
 MOV ACC DOWN
 SWP # LENGTH
 SUB 1
 JGZ LOOP
 
@2

@3

@4

@5
 MOV 0 DOWN
  MOV ACC DOWN
   SWP
    MOV 30 ACC
LOOP: MOV UP DOWN
 SUB 1
 JGZ LOOP
 MOV -1 DOWN
 SWP # ROW
 ADD 1
 
@6

@7

@8

@9
 MOV UP RIGHT
 
@10
 MOV LEFT DOWN
 
@11

```