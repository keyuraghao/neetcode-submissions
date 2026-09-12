class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} #val:index

        for i in range(len(nums)):
            req = target - nums[i]
            if req in seen:
                return [seen[req],i]
            else:
                seen[nums[i]] = i