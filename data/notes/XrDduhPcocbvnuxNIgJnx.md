## Problem

This question is asked by Google.

Given an array of integers, return whether or not two numbers sum to a given target, k.

Note: you may not sum a number with itself.

Ex: Given the following...

> [1, 3, 8, 2], k = 10, return true (8 + 2)
>
> [3, 9, 13, 7], k = 8, return false
>
> [4, 2, 6, 5, 2], k = 4, return true (2 + 2)

## [[python]]

```python
def twoSum(nums: List[int], target: int) -> List[int]:
    num_map = {}
    for idx,x in enumerate(nums):
        if target-x in num_map:
            return true
            #return[idx,num_map[target-x]]
        else:
            num_map[x] = idx

```

## [[go]]

```go
func twoSum(nums []int, target int) []int {
    var seen  = make(map[int]int)
    for i,v := range nums{
        idx := target - v
        _,exists := seen[idx]
        if exists {
            return true
            //return []int{i,seen[idx]}
        }
        seen[v]=i
    }
    return[]int{}
}
```

## [[rust]]

