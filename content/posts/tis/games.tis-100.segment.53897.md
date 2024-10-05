+++
title = "TIS-100 Segment : 53897"
date = "2022-11-13T10:27:17.767000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Histogram Viewer

### Solution

![](/images/games/tis-100/segment/53897/1.png) 

### Solution

```
@0

@1
MOV UP DOWN

@2

@3

@4

@5
MOV UP DOWN

@6

@7

@8

@9
MOV UP RIGHT

@10
DY: MOV LEFT ACC
X: SWP
 MOV ACC DOWN
 SWP
 NEG
 ADD 18
Y: MOV ACC DOWN
 MOV 3 DOWN
 MOV -1 DOWN
 NEG
 ADD 17
 JGZ X
 SWP
 ADD 1
 SAV
 
@11

```