# Leetcode-Algorithim-Python
Solutions for several Leetcode algorithm problems using Python

## Easy Problems

### 1. Two Sum
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

```
Example:
Given nums = [2, 7, 11, 15], target = 9,
Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
```

Code:

```Python
def twoSum(nums):
  for i in range(len(nums)):
    lkup = target - nums[i]
    if lkup in nums:
      k = nums.index(lkup)
      if i!=k:
        return [i,k]
      else:
        continue
```

### 53. Maximum Subarray
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

```
Example:
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

Code:
```Python
def maxSubArray(nums):
  carry = nums[0]
  max_sum = nums[0]

  for x in nums[1:]:
    carry = max(x,x+carry)
    max_sum = max(max_sum,carry)
  return max_sum
```
