---
id: EawxKL2ZJLE1J6H5d789t
title: Quick Sort
desc: ''
updated: 1641425420524
created: 1641343988473
---
# Quick Sort

It is a Divide and Conquer Algorithm.

Pick an element in the array as `pivot` and move all elements less than pivot to its left and all elements greater to its right


## Time Complexity

### Best: O(nlog(n))

### Average: O(nlog(n))

### Worst: O(n*n)

## Space Complexity: O(log(n))

# Implementation

## [[python]]

```python
def quickSort(nums):
    quickSortHelper(nums, 0, len(nums)-1)


def quickSortHelper(nums, low, high):
    if low < high:
        partitionIdx = partition(nums, low, high)
        quickSortHelper(nums, low, partitionIdx-1)
        quickSortHelper(nums, partitionIdx+1, high)


def partition(nums, low, high):
    ptr = low
    pivot = nums[ptr]
    while low < high:
        while low < len(nums) and nums[low] <= pivot:
            low = low + 1
        while nums[high] > pivot:
            high = high - 1
        if low < high:
            nums[low], nums[high] = nums[high], nums[low]
    print(high, ptr)
    nums[high], nums[ptr] = nums[ptr], nums[high]
    return high


array = [10, 7, 8, 9, 1, 5]
quickSort(array)
print(array)


```