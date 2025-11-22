#Problem 217 - Contains Duplicate

#Problem Description
'''
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

Example 1:

Input: nums = [1,2,3,1]
Output: true
Explanation:
The element 1 occurs at the indices 0 and 3.

Example 2:
Input: nums = [1,2,3,4]
Output: false
Explanation:
All elements are distinct.

Example 3:
Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
'''

#Thought Process
'''
The quickest way to do this would be to achieve this in one sweep. My initial attempt is to compare the length of the set(nums) and nums itself since set() 
removes the duplicate: if len(set(nums)) < len(nums): return True; return False. Although this works, it is slow because taking the length itself guarantees
going over all elements, making the time and space complexity O(n), and not really one sweep. 

To make this truly one sweep, I should populate the set one element at a time, and before I populate it with a new element, ask if I have seen this element 
before. This should mean that, worst case scenario, it is O(n) in time and space complexity, but it is much faster as it is truly one sweep.
'''

#Code - Attempt 1
def containsDuplicate_1(nums):
    set_nums = set(nums) #Removes duplicates
    if len(set_nums) < len(nums):
        return True
    return False

#Code - Attempt 2
def containsDuplicate_2(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False

