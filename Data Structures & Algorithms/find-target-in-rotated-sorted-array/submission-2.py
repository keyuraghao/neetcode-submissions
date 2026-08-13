class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # this is similar to the min value in the rotated sorted arr

        # following is the simple solution for in the time O(n)
        # ans = -1
        # for i in range(len(nums)):
            # if nums[i] == target:
                # ans = i
                # return ans
        # return ans

        # The big brains will optimze the solution to be done in O(log n) time
        # this technique uses the binary search concept as the arr was sorted
        left = 0
        right = len(nums) -1 

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # going to left side
            if nums[left] <= nums[mid]:
                if target > nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1
            
            # goind to the right side
            else:
                if target < nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1
        return -1