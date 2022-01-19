# -*- coding: utf-8 -*-

class Solution:
# Write your code here
    def pushCharacter(self, palabra):
        a = ""
        a += palabra
        return a

    def enqueueCharacter(self, palabra):
        b = ""
        a = len(palabra)
        for x in range(a):
            a -= 1
            b += palabra[a]
        return b

# read the string s
s = input()
# Create the Solution class object
obj = Solution()
l = len(s)

# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])

isPalindrome = True
''''
pop the top character from stack
dequeue the first character from queue
compare both the characters
'''
if obj.enqueueCharacter(s) != obj.pushCharacter(s):
    isPalindrome = False

# finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, " + s + ", is a palindrome.")
else:
    print("The word, " + s + ", is not a palindrome.")
