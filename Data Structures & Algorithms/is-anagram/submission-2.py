class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hash_map = {} # char : count

        for val in s:
            if val in hash_map:
                hash_map[val] += 1
            else:
                hash_map[val] = 1
        
        for val in t:
            if val not in hash_map:
                return False
            else:
                hash_map[val] -= 1
                if hash_map[val] == 0:
                    del hash_map[val]
        return len(hash_map) == 0
