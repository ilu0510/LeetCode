#Problem 20 - Valid Parentheses

#Problem Description
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true
'''

#Thought Process
'''
'''

#Code - Attempt 1

def isValid(s):
    brackets = {")" : "(", "]" : "[", "}" : "{"}
    stack = []
    for i in s:
        if i in brackets:
            if stack and stack[-1] == brackets[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return True if not stack else False
            