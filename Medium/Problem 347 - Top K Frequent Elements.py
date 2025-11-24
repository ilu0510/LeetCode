#Problem 347 - Top K Frequent Elements

#Problem Description
'''
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Example 3:
Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
Output: [1,2]

'''

#Thought Process
'''
The Brute force method seems like I can essentially to do a frequency table, i.e. a dictionary with the key being the number and value being the frequency - go through each number and increment the count for each number.
But then I would have to sort my dictionary to find the k most frequent elements so that seems incredibly slow, O(nlogn), and space complexity is O(n). I will build it anyway before I take a hint. 

NeetCode suggests bucket sort. I will search up just the algorithm first and then figure out a way to implement it. From what I understand, I am thinking of making the frequency the bucket number, and the numbers would be 
the data I am sorting. So if something is repeated once, it falls in the first bucket; if something is repeated 3 times it falls in the third bucket. So this would mean implementing a dictionary with the key being the frequency 
and the values being the list of numbers. And since we want the top K arrays, we will start at the last bucket and work backwards to output the number. Since the max size of the array of buckets is constrained to the number of 
elements in the nums array, time complexity is O(n) and space complexity is O(n).
'''

#Code - Attempt 1
def topKFrequent_1(nums, k):
    h = {}
    for i in nums:
        h[i] = h.get(i,0)+1 #Creates frequency table
    
    sort_h = sorted(h.items(), key=lambda item: item[1], reverse=True) #Sorting in descending order of value

    return [num for (num, frquency) in sort_h[:k]] #Take the first k items from the sort_h and extract only the numbers (not their frequencies)
        
#Code - Attempt 2
def topKFrequent_2(nums, k):
    h = {}
    for n in nums:
        h[n] = h.get(n,0)+1
    
    bucket = {} 
    for num, freq in h.items():
        if freq not in bucket:
            bucket[freq] = []
        bucket[freq].append(num)
    
    res = []
    max_freq = max(bucket.keys())

    for i in range(max_freq, 0, -1):
        if i in bucket:
            for num in bucket[i]:
                res.append(num)
            if len(res)==k:
                return res
    return res

    












        





