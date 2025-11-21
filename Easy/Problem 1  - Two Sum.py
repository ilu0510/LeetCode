#Problem 1 - Two Sum

#Problem Description
'''
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''

#Thought Process
'''
I should take the difference between the target and nums[i], and store the result as a value in the hashmap, with the key being nums[i] and 
the difference is the value. Then when we move onto the next number in the array, we can check if that number exists in the hashmap; if it 
does, then we are done; if not, we continue the process till we find one.

Since we need to return the index, we will have to use enumerate. 

Since this is a hashmap, the time and the space complexity is dependent on the size the nums array, hence it is O(n) for both.  
'''

def twoSum(nums, target):
    h = {} #Setting up the hashmap
    for i, n in enumerate(nums): #Gives the index and the number in nums associated to the index
        diff = target - nums[i] 
        if diff in h: #Check if difference is in the hashmap
            return [h[diff],i] #return the index of the pair that gives you the target
        h[n] = i #key-value pair: key = number, i = index

