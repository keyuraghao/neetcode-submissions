class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        result = len(nums)
        for idx,val in enumerate(nums):
            result = result ^ idx ^ val
        return result