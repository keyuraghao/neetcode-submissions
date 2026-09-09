class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hash_set = set()
        for val in nums:
            if val in hash_set:
                return True
            else:
                hash_set.add(val)
        return False
