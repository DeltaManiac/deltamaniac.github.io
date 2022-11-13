## Interrupt Handler

# Solution

```
@0
START:
MOV UP,ACC
JGZ CHECK
SWP
JMP NEXT

CHECK:
SWP
JGZ NEXT
MOV 1,DOWN
JMP START

NEXT:
MOV 0,DOWN

@1
START:
MOV UP,ACC
JGZ CHECK
SWP
JMP NEXT

CHECK:
SWP
JGZ NEXT
MOV 2,DOWN
JMP START

NEXT:
MOV 0,DOWN

@2
START:
MOV UP,ACC
JGZ CHECK
SWP
JMP NEXT

CHECK:
SWP
JGZ NEXT
MOV 3,DOWN
JMP START

NEXT:
MOV 0,DOWN

@3
START:
MOV UP,ACC
JGZ CHECK
SWP
JMP NEXT

CHECK:
SWP
JGZ NEXT
MOV 4,DOWN
JMP START

NEXT:
MOV 0,DOWN

@4
MOV UP,RIGHT

@5
MOV UP,RIGHT
MOV LEFT,RIGHT

@6
ADD UP
ADD RIGHT
ADD LEFT
ADD LEFT
MOV ACC,DOWN
MOV 0,ACC

@7
MOV UP,LEFT

@8

@9
MOV UP,DOWN

@10

@11

```

# Solution

![](/assets/images/2022-11-12-21-46-16.png)