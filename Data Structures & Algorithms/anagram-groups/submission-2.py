from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list) # key = (character:count) : strings

        for string in strs:
            key = [0]*26
            for i in string:
                key[ord(i) - ord('a')] += 1
            hash_map[tuple(key)].append(string)
        return list(hash_map.values())