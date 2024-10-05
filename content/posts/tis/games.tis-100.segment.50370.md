+++
title = "TIS-100 Segment : 50370"
date = "2022-11-12T22:44:31.956000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Image Test Pattern 1

### Solution

![](/images/games/tis-100/segment/50370/1.png) 

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
COL: 
MOV 0,DOWN
ROW: 
MOV ACC,DOWN
MOV 30,ACC
PXL: 
MOV 3,DOWN
SUB 1
JNZ PXL
END: 
MOV -1,DOWN
SWP
ADD 1
SAV

@11

```