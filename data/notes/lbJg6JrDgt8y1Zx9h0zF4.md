## Problem

Write a function that takes two arrays as inputs and returns to us their intersection?

Ex

> const nums1 = [1, 2, 2, 1];
> const nums2 = [2, 2];
>
> intersection(nums1, nums2);
> // [2]

**Constraints**

- Length of the array &lt;= 100000
- The values in the array will be in the range -1000000000 and 1000000000
- Expected time complexity: O(n+m) where n and m are the lengths of the array.
- Expected space complexity: O(max(n,m)).

  ## [[python]]

```python
def intersection(arr1,arr2):
    return list(set(arr1).intersection(set(arr2)))
```
