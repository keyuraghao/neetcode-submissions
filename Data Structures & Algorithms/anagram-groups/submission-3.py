from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) #tuple(key) : [elements of the strs]

        for val in strs:
            key = [0]*26
            for char in val:
                key[ord(char) - ord('a')] += 1
            
            hash_map[tuple(key)].append(val)
        
        return list(hash_map.values())