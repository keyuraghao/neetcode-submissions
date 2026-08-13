class Solution:
    def findMin(self, nums: List[int]) -> int:
        # following is the simple O(n) solution:
        minn = nums[0]
        for i in nums:
            minn = min(minn,i)
        return minn
        
        # left = 0
        # right = len(nums) - 1
        # minn = nums[left]
        # while left <= right:
            # if nums[left] < nums[right]:
                # minn = min(nums[left], minn)
                # break
            # mid = (left + right) // 2
            # minn = min()
             