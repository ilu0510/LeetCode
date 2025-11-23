#Problem 49 - Group Anagrams

#Problem Description
'''
Given an array of strings strs, group the together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Explanation:
    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

'''

#Thought Process
'''
The easiest way to do this is to sort the strings and then compare. Sorting has a time complexity of nlog(n), which is quite slow.
Since I need to return an array, and want something that is fast to lookup and add, I will pick a hashmap. So what should I use as the key and value?
I am thinking, I can have an array of zeroes that has length 26 to represent the alphabets, that are incremented by 1 for every occurence. But how do I know what the index is?
I can simply just use the ord function to find its corresponding unicode integer. 
We will use this as a way to compare the similarities: for each array, they group the anagrams based on 
So, our keys will be the array and their values will be the words. I just have to make sure that I turn the array into a tuple since lists are non-hashable. 
We will then just return the values. 
In order to make this hashmap, we will use defaultdict to deal with the edge case of missing keys.

Since I am looping through the array with n number of words, with each word having m letters, the time complexity becomes O(m * n).
Since I have a maximum of 26 letters, the space complexity becomes O(1)
'''

#Code - Attempt 1
from collections import defaultdict
def groupAnagrams_1(str):
    d = defaultdict(list)
    for s in str:
        counter = [0]*26 
        for i in s:
            counter[ord(i)-ord("a")] += 1 #Finding the index for the alphabet, and incrementing for the occurence
        d[tuple(counter)].append(s) #Inserting the value for the given key. Turning into tuple since arrays not hashable
    return list(d.values())




        





