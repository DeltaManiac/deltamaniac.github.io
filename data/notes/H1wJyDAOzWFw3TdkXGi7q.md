## Problem

Design a class to implement a stack using only a single queue.

Your class, `QueueStack`, should support the following stack methods: `push()` (adding an item), `pop()` (removing an item), `peek()` (returning the top value without removing it), and `empty()` (whether or not the stack is empty).

## [[python]]

```python
Class QueueStack:
    def __init__(self):
        self.q = []

    def append(self,val):
        size = len(self.q)
        q.append[val]
        for i in range(size):
            q.append(q.pop(0))

    def pop(self):
        if len(self.q)==0:
            return None
        else:
            return self.q.pop(0)

    def peek(self):
        if len(self.q)==0:
            return None
        else:
            return self.q[-1]

    def empty(self):
        return len(self.q)==0
```

## [[go]]

## [[rust]]

