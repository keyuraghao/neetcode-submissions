from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict()
        for val in s:
            if val in seen:
                seen[val] += 1
            else:
                seen[val] = 1
        
        for val in t:
            if val in seen:
                seen[val] -= 1
                if seen[val] == 0:
                    del seen[val]
            else:
                return False
        
        return len(seen) == 0