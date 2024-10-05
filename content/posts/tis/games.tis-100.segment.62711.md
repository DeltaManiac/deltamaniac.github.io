+++
title = "TIS-100 Segment : 62711"
date = "2022-11-13T10:37:05.371000+05:30"
tags = ["games", "TIS-100"]
draft = false
type = "post"
+++

# Sequence Indexer

### Solution

![](/images/games/tis-100/segment/62711/1.png) 

### Solution

```
@0
MOV UP    ACC
JGZ B
SWP
MOV 0     RIGHT
ADD 1
MOV ACC   DOWN
A: JMP A
B: MOV ACC   RIGHT
SWP
ADD 1
SAV

@1

@2
MOV UP    DOWN

@3

@4
MOV UP    RIGHT

@5
   MOV LEFT  ACC
   SAV
B: MOV UP    DOWN
   SUB 1
   JGZ B
C: MOV DOWN  ACC
MOV ACC   RIGHT
   MOV ACC   UP
   JGZ C
   SWP
   SAV
   JMP B
   
@6
  MOV UP    ACC
   JEZ B
A: MOV LEFT  NIL
   SUB 1
   JGZ A
B: MOV LEFT  DOWN
C: MOV LEFT  ACC
   JGZ C
   
@7

@8

@9
MOV UP    DOWN

@10

@11

```