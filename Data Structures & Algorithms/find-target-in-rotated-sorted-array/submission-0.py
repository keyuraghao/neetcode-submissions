class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is similar to the min value in the rotated sorted arr

        # following is the simple solution for in the time O(n)
        ans = -1
        for i in range(len(nums)):
            if nums[i] == target:
                ans = i
                return ans
        return ans