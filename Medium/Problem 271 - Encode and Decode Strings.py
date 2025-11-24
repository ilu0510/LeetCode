#Problem 271 - Encode and Decode Strings

#Problem Description
'''
Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and is decoded back to the original list of strings.
Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output: ["neet","code","love","you"]
Explanation:
One possible encode method is: "lint:;code:;love:;you"
'''

#Thought Process
'''
Cannot concatenate for encode because it would be impossible to decode. I need to also be aware that the user can input punctuations and numbers too, so I need 
a more robust delimiter.
I could potentially use the number of characters in a string and a symbol as means to delimit. This should sort out encoding. 
To decode, I simply need to find the number and the delimiter as means to understand where the first part of the input message starts and ends. 
'''

#Code - Attempt 1

def encode(message):
    delimit = "|"
    encoded = ""
    for i in message:
        encoded += str(len(i)) + delimit + i
    return encoded

def decode(message):
        delimit = "|"
        out = []
        i = 0

        while i < len(message):
            # 1) Find the delimiter starting from i, not from 1
            mark = i
            while message[mark] != delimit:
                mark += 1

            # 2) Parse the length
            valid_message = int(message[i:mark])

            # 3) Jump to the start of the actual string
            i = mark + 1
            end = i + valid_message

            # 4) Slice out the string
            out.append(message[i:end])

            # 5) Move i to the end for the next iteration
            i = end

        return out



 