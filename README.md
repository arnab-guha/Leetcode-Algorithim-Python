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
### 21. Merge Two Sorted Lists
Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.
```
Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
```

Code:
```Python
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
  root = c = ListNode(0)  
  while l1 and l2:
    if l1.val<l2.val:
      c.next = l1
      l1 = l1.next
    else:
      c.next = l2
      l2 = l2.next
    c = c.next
  c.next = l1 or l2
  return root.next
```

### 20. Valid Parentheses
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.
```
Example 1:

Input: "()"
Output: true
Example 2:

Input: "()[]{}"
Output: true

Example 3:

Input: "(]"
Output: false
Example 4:

Input: "([)]"
Output: false
Example 5:

Input: "{[]}"
Output: true
```
Code:
```Python
def isValid(s):
  d = {'}':'{',']':'[',')':'('}
  stack = []

  for x in s:
    if stack and (x in d and stack[-1]==d[x]):
      stack.pop()
    else:
      stack.append(x)
  return not stack
```

### 937. Reorder Data in Log Files
You have an array of logs.  Each log is a space delimited string of words.

For each log, the first word in each log is an alphanumeric identifier.  Then, either:

Each word after the identifier will consist only of lowercase letters, or;
Each word after the identifier will consist only of digits.
We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

Return the final order of the logs.


```
Example 1:

Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
```
Code:
```Python
def reorderLogFiles(self, logs: List[str]) -> List[str]:
  letter = []
  number = []
  for x in logs:
    if x.split()[1].isalpha():
      letter.append(x)
    else:
      number.append(x)
  letter.sort(key=lambda letter: (letter.split()[1:],letter.split()[0]))
  return letter+number
```
