---
id: s4VCxV9Bg3TNzXGBonKY1
title: Selection Sort
desc: ''
updated: 1641311805207
created: 1641310120941
---

# Selection Sort

Selection sort finds the smallest element in the array and place it on the first place on the list, then it finds the second smallest element in the array and place it on the second place.


## Time Complexity

### Best: O(n*n)

### Average: O(n*n)

### Worst: O(n*n)

## Space Complexity: O(1)

# Implementation

# [[python]]

```python
def selectionSort(arr):
    for i in range(len(arr)):
        minIdx = 1
        for j in range(i+1,len(arr)):
            if arr[minIdx]>arr[j]:
                arr[minIdx], arr[j] = arr[j], arr[minIdx]

a = [64, 25, 12, 22, 11]
selectionSort(a)
print(a) #[11, 12, 22, 25, 64]

```

