class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {} #num : index

        for i in range(len(nums)):
            need = target - nums[i]
            if need in hash_map:
                return [hash_map[need],i]
            else:
                hash_map[nums[i]] = i