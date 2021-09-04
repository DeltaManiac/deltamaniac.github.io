---
id: oBXH1mHBh4xsA5Cll2r1c
title: Merge Sorted Linked Lists
desc: ''
updated: 1629039673383
created: 1629038995187
nav_order: 15
---

# Problem
This question is asked by Apple.

Given two sorted linked lists, merge them together in ascending order and return a reference to the merged list

Ex: Given the following lists...

> list1 = 1->2->3, list2 = 4->5->6->null, return 1->2->3->4->5->6->null
>
> list1 = 1->3->5, list2 = 2->4->6->null, return 1->2->3->4->5->6->null
>
> list1 = 4->4->7, list2 = 1->5->6->null, return 1->4->4->5->6->7->null

## [[python]]

```python
class LinkedList:
    def __init__(self,value):
        self.value = value
        self.next = None

def mergeLists(h1,h2):
    ptr1 = h1
    ptr1_prev =None
    ptr2 = h2
    while ptr1 is not None and ptr2 is not None:
        if ptr1.value < ptr2.value:
            ptr1_prev = ptr1
            ptr1 = ptr1.net
        else:
            if ptr1_prev is not None:
                ptr1_prev.next = ptr2
            ptr1_prev = p2
            ptr2 = ptr2.next
            ptr1_prev.next = ptr1
    if ptr1 is None:
        ptr1_prev.next = ptr2
    return h1 if h1.value < h2.value else h2
```
## [[go]]

## [[rust]]
