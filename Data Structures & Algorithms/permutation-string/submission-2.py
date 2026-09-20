from collections import defaultdict
# this is the solution using the hashmap
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        s1_count = defaultdict(int)
        window = defaultdict(int)

        for i in range(len(s1)):
            s1_count[s1[i]] += 1
            window[s2[i]] += 1
        
        if window == s1_count:
            return True
        left = 0
        for right in range(len(s1), len(s2)):
            window[s2[right]] += 1 
            window[s2[left]] -= 1
            if window[s2[left]] ==0:
                del window[s2[left]]
            if window == s1_count:
                return True
            left += 1
        return False 