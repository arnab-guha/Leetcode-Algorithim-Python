#Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

#Example:

#Input: [-2,1,-3,4,-1,2,1,-5,4],
#Output: 6
#Explanation: [4,-1,2,1] has the largest sum = 6.

def maxSubArray(self, nums: List[int]) -> int:
    carry = nums[0]
    max_sum = nums[0]
    
    for x in nums[1:]:
        carry = max(x,x+carry)
        max_sum = max(max_sum,carry)
    return max_sum
