class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sett = set(nums)
        longest = 0

        for n in nums:
            if (n-1) not in sett:
                length = 0
                while (n+length) in sett:
                    length += 1
                
                longest = max(longest,length)
        return longest
# time : O(n)
# space : O(n)