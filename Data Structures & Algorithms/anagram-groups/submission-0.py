from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hash_map = defaultdict(list)

        for words in strs:
            count_key = [0]*26
            for i in words:
                count_key[ord(i) - ord('a')] += 1
            hash_map[tuple(count_key)].append(words)
        return list(hash_map.values())