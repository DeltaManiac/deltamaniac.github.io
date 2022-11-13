## Stored Image Decoder

# Solution

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

# Solution

![](/assets/images/2022-11-13-10-43-52.png)

