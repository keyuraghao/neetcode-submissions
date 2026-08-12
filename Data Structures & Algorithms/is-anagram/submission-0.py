class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}

        for i in range(len(s)):
            if s[i] in seen:
                seen[s[i]] += 1
            else:
                seen[s[i]] = 1
        
        for i in range(len(t)):
            if t[i] not in seen:
                return False
            else:
                seen[t[i]] -= 1
                if seen[t[i]] == 0:
                    del seen[t[i]]
        
        return len(seen) == 0