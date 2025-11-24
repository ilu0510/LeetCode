#Problem 238 - Product of Array Except Self

#Problem Description
'''
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
'''

#Thought Process
'''
The easiest way I see this be solved is if you multiply everything but nums[i]; however, this would give us a time complexity of O(n^2).
I need a way to remove redundant calculations. I will consider NeetCode's hint: We can use the prefix and suffix technique. First, we iterate from left to right and store the prefix products for each index in a prefix array, 
excluding the current index's number. Then, we iterate from right to left and store the suffix products for each index in a suffix array, also excluding the current index's number.
With this in mind, I see it play out like:
nums = [a,b,c,d,e]
prefix: |a|, |ab|, |abc|, |abcd|, |abcde|
suffix: |e|, |de|, |cde|, |bcde|, |abcde|
i=0: suffix[3]
i=1: prefix[0]*suffix[2]
i=2: prefix[2]*suffix[2]
i=3: prefix[3]*suffix[1]
i=4: prefix[3]
This means my algorithm has a time and space complexity of O(n).

Looked at NeetCode's solution which has a time complexity of O(n) but a space complexity O(1). Instead of having a separate prefix and suffix array, NeetCode has a singular output array res that stores the prefix products, 
then does a backward pass with a running suffix product product and multiply into res. 
'''

#Code - Attempt 1
def productExceptSelf_1(nums):
    prefix = []
    suffix = []
    prod_front = 1
    prod_back = 1
    res = []
    for i in range(len(nums)):
        prod_front *= nums[i]
        prefix.append(prod_front)

        prod_back *= nums[len(nums)-1-i]
        suffix.append(prod_back)

    res.append(suffix[len(nums)-2])
    for i in range(len(nums)-2):
        res.append(prefix[i]*suffix[len(nums)-3-i])
    res.append(prefix[len(nums)-2])

    return res

#Code - Attempt 2 (NeedCode's Solution)
def productExceptSelf_2(nums):
        res = [1] * (len(nums)) #Create the result array filled with 1s.
        prefix = 1 #prefix will store the running product of all elements to the LEFT of i
        #First pass: fill res[i] with the prefix product
        for i in range(len(nums)):
            res[i] = prefix #assign product of all nums before index i
            prefix *= nums[i] #update prefix to include nums[i]
        
        postfix = 1 #postfix will store the running product of all elements to the RIGHT of i
        #Second pass (right to left): multiply each res[i] by the postfix product
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix #multiply by product of all nums after index i
            postfix *= nums[i] #update postfix to include nums[i]
        return res






        



    












        





