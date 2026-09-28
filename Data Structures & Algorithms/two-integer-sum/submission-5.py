class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {} # val : index

        for idx, val in enumerate(nums):
            req = target - val
            if req in seen:
                return [seen[req],idx]
            else:
                seen[val] = idx
            