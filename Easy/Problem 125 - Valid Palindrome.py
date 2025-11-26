#Problem 128 - Longest Consecutive Sequence

#Problem Description
'''
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same 
forward and backward. Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.

Example 3:
Input: s = " "
Output: true
Explanation: s is an empty string "" after removing non-alphanumeric characters.
Since an empty string reads the same forward and backward, it is a palindrome.

'''

#Thought Process
'''

'''

#Code - Attempt 1

def alphaCheck(character):
    return (ord('A') <= ord(character) <= ord('Z') or ord('a') <= ord(character) <= ord('z') or ord('0') <= ord(character) <= ord('9'))


def isPalindrome(s):
    l = 0
    r = len(s) - 1

    while l < r:
        while l < r and not alphaCheck(s[l]):
            l +=1
        while r > l and not alphaCheck(s[r]):
            r -=1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True
        
        





