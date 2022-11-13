---
id: zn6yh2g7c7m27m7spggt3fl
title: '62711'
desc: ''
updated: 1668316107974
created: 1668316025371
---
## Sequence Indexer

# Solution

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

# Solution

![](/assets/images/2022-11-13-10-38-24.png)