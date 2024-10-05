+++
title = "TIS-100 Segment : 41427"
date = "2022-11-12T22:13:02.597000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Sequence Peak Detector

### Solution

![](/images/games/tis-100/segment/41427/1.png)

### Solution

```
@0

@1
MOV UP,ACC
MOV ACC,RIGHT
MOV ACC,DOWN

@2
MOV LEFT,DOWN

@3

@4

@5
MOV UP ,ACC
MOV ACC,DOWN
MOV ACC,DOWN

@6
MOV UP,ACC
MOV ACC,DOWN
MOV ACC,DOWN

@7

@8

@9
MOV 999,ACC
IN:
SAV
SUB UP
JGZ NEW
ADD UP
JMP IN

NEW:
MOV UP,ACC
JGZ IN

OUT:
SWP
MOV ACC,DOWN

@10
IN:
SAV
SUB UP
JLZ NEW
MOV UP,ACC
JEZ OUT
SWP
JMP IN
NEW: 
MOV UP,ACC
JGZ IN

OUT: SWP
MOV ACC,DOWN
MOV 0,ACC

@11

```