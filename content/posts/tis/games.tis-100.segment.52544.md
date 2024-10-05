+++
title = "TIS-100 Segment : 52544"
date = "2022-11-13T08:09:55.828000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Exposure Mask Viewer

### Solution

![](/images/games/tis-100/segment/52544/1.png) 

### Solution

```
@0

@1
 MOV UP RIGHT

@2
X0: MOV LEFT DOWN
Y0: MOV LEFT ACC
 SAV
DX: MOV LEFT DOWN
DY: MOV LEFT ACC
LOOP: SWP
Y: MOV ACC DOWN
 ADD 1
 SWP
 MOV ACC DOWN
 SUB 1
 JGZ LOOP
 
@3

@4

@5

@6
INIT: MOV UP ACC
 SAV
 MOV UP ACC
 SUB 6
 NEG
 SWP
X0: MOV ACC DOWN
Y:  MOV UP DOWN
 SWP
DX: MOV ACC DOWN
 SWP
 JRO UP
 JMP INIT
 JMP X0
 
@7

@8

@9

@10
X0: MOV UP DOWN
Y:  MOV UP DOWN
MOV 3 DOWN
DX: JRO UP
5:  MOV 3 DOWN
4:  MOV 3 DOWN
3:  MOV 3 DOWN
2:  MOV 3 DOWN
1:  MOV -1 DOWN

@11

```