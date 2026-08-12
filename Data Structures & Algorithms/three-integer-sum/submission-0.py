class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        target = 0
        nums.sort()

        for idx, val in enumerate(nums):
            if idx > 0 and val == nums[idx - 1]:
                continue
            
            left = idx + 1
            right = len(nums) - 1

            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total > target:
                    right -= 1
                elif total < target:
                    left += 1
                else:
                    ans.append([nums[idx],nums[left],nums[right]])
                    left += 1
                    while nums[left] == nums[left -1 ] and left < right:
                        left += 1
        return ans
        