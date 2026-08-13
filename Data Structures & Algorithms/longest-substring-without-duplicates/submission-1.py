class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        left = 0
        right = 0
        longest_length = 0

        while right < len(s):
            while right < len(s) and s[right] not in seen:
                seen.add(s[right])
                right += 1
            curr_length = right - left
            longest_length = max(curr_length,longest_length)
            while right < len(s) and s[right] in seen:
                seen.remove(s[left])
                left += 1
        
        return longest_length

        # Time complexity : O(n) iterating only 1 time 
        # space complexity : O(1) only the vairiable and the ans(longest_length) is being stored

        