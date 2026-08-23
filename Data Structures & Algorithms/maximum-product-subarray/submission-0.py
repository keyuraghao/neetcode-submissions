class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = max(nums)
        curr_min = 1
        curr_max = 1

        for n in nums:
            temp = n * curr_max
            curr_max = max(curr_max * n, curr_min * n, n)
            curr_min = min(temp,curr_min * n, n)
            ans = max(ans,curr_max)
        return ans