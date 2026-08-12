class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # if you directly sort the nums arr the solution will take O(n log n) time which is bad 

        # following is the solution for time O(n)

        nums_set = set(nums)
        ans = 0
        for i in nums:
            if (i-1) not in nums_set:
                length = 0
                while (i+length) in nums_set:
                    length += 1
                ans = max(length,ans)
        return ans