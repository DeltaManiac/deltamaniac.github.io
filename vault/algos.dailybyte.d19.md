---
id: 7Hc5ffEoLnA0BZkmQW0ww
title: Has Cycle ?!
desc: ''
updated: 1629418318120
created: 1629418216065
nav_order: 19
---
## Problem

This question is asked by Microsoft.

Given a linked list, containing unique numbers, return whether or not it has a cycle.

Note: a cycle is a circular arrangement (i.e. one node points back to a previous node)

Ex: Given the following linked lists...

> 1->2->3->1 -> true (3 points back to 1)
>
> 1->2->3 -> false
>
> 1->1 true (1 points to itself)

## [[python]]

```python
def hasCycle(self, head: ListNode) -> bool:
    if not head: return False
    if head.next is None:
        return False

    ptr = head.next
    if head.next.next is None:
        return False
    cur = head.next.next
    while cur != ptr:
        if cur is None or cur.next is None:
            return False
        ptr = ptr.next
        cur = cur.next.next
    return True
```

## [[go]]

## [[rust]]

