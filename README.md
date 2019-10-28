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
def reorderLogFiles(logs):
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

### 206. Reverse Linked List
Reverse a singly linked list.

Example:
```
Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL
```
Code:
###### Hint: Use a prev variable to hold the previous node and reverse the next node pointer to previous node.

```Python
def reverseList(self, head: ListNode) -> ListNode:
  prev = None
  while head:
    temp = head
    head = head.next
    temp.next = prev
    prev = temp
  return prev
```

### 202. Happy Number
Write an algorithm to determine if a number is "happy".

A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

```
Example:

Input: 19
Output: true
Explanation:
1^2 + 9^2 = 82
8^2 + 2^2 = 68
6^2 + 8^2 = 100
1^2 + 0^2 + 0^2 = 1
```
Code:
###### Hint: sum of square of the digits of a number will result in a repeating number which will help to break the infinite loop.

```Python
def isHappy(self, n: int) -> bool:
  seen=[]
  while n not in seen:
    seen.append(n)
    n = sum([int(i)**2 for i in str(n)])
  return n==1
```

### 121. Best Time to Buy and Sell Stock
Say you have an array for which the ith element is the price of a given stock on day i.

If you were only permitted to complete at most one transaction (i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.

Note that you cannot sell a stock before you buy one.
```
Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
```

Code:
```Python
def maxProfit(prices):
  if prices:
    maxprofit = 0
    minprice = prices[0]
    for x in prices:
      minprice = min(minprice,x)
      profit = x-minprice
      maxprofit= max(maxprofit,profit)
    return maxprofit
  else:
    return 0
"""
  if prices:
    gp = 0
    for i in range(len(prices)-1):
      p = max(prices[i+1:])-prices[i]
      gp = max(gp,p)
    return gp
  else:
    return 0
"""        
```    
