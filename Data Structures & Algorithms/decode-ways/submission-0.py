class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1} # no. of chosen characters : no. of ways we can decode them (ex. if we take all the characters from the given string that is len(s) then there are no other characters remaining and we can do this in exactly one way)

        def dfs(i):
            if i in dp: # return the value stored in the dp dict for a length we have already calculated
                return dp[i]
            if s[i] == "0": # because there is no mapping of 0 in the given encoding and this is a bogus case
                return 0 
            
            ans = dfs(i+1)
            if (i+1 < len(s) and (s[i] == "1" or s[i] == "2" and s[i+1] in "0123456")):
                ans += dfs(i+2)
            dp[i] = ans 
            return ans

        return dfs(0)