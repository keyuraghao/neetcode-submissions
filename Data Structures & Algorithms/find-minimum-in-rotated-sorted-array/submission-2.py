# this means that we need to find the start of the rotated sorted array
class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        minn = nums[left]
        while left <= right:
            if nums[left] < nums[right]:
                minn = min(minn,nums[left])
                break
            
            mid = (left + right) // 2
            minn = min(minn,nums[mid])
            if nums[mid] >= nums[left]:
                left = mid + 1
            else:
                right = mid - 1
        
        return minn