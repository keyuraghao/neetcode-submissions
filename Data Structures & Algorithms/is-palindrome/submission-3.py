# this can be solved in 2 different ways
1. 
class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        for c in s:
            if c.isalnum():
                newstr += c.lower()
        
        return newstr == newstr[::-1]