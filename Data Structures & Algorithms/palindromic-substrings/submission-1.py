class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0

        def checker(left,right):
            temp = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
                temp +=1
            return temp
        
        for i in range(len(s)):
            ans += checker(i,i)
            ans += checker(i,i+1)
        return ans