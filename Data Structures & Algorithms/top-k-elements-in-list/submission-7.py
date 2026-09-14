# this is the second solution with time O(n)
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        n = len(nums)
        # initializing the counter can also be done using the Cunter from the collections
        for val in nums:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1

        buckets = [0] * (n+1)

        for num, freq in counter.items():
            if buckets[freq] == 0:
                buckets[freq] = [num]
            else:
                buckets[freq].append(num)
        
        ret = []
        for i in range(n,-1,-1):
            if buckets[i] !=0:
                ret.extend(buckets[i])
            if len(ret) == k:
                break
        
        return ret
