#Problem 242 - Valid Anagram

#Problem Description
'''
Given two strings s and t, return true if t is an of s, and false otherwise.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

'''

#Thought Process
'''
The easiest way to do this is to sort the strings and then compare. Sorting has a time complexity of nlog(n), which is quite slow. 
I should first make it clear at the start that if the number of letters are not the same, then it obviously will not be an anagram.
I can set up a hashmap where the letter is the key and the number of occurences of that letter is the value. If this matches for s and t, then they are anagrams.

Given that I have to loop through the letters, if s has n and t has m number of letters, my time complexity becomes O(n + m).
Since I have only a possiblity of 26 letters to pick from, my space complexity is O(1).
'''

#Code - Attempt 1
def isAnagram_1(s,t):
    if len(s) != len(t): 
        return False #Unequal number of letters => cannot be anagrams
    
    h_s = {}
    h_t = {} 
    for i in s:
        h_s[i] = h_s.get(i,0)+1 #Creates a key (the letter) and a value which gets incremented by one for every occurence
    for i in t:
        h_t[i] = h_t.get(i,0)+1
    
    return h_s == h_t 

#While the code works, I should be able to do it in one loop 
def isAnagram_2(s,t):
    if len(s) != len(t): 
        return False #Unequal number of letters => cannot be anagrams
    
    h_s = {}
    h_t = {} 
    for i in range(len(s)):
        h_s[s[i]] = h_s.get(s[i],0)+1
        h_t[t[i]] = h_t.get(t[i],0)+1
    
    return h_s == h_t 

    