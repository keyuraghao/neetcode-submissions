import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # solution using heapq
        counter = {} #number : count of the number
        heap = []

        for val in nums:
            if val in counter:
                counter[val] += 1
            else:
                counter[val] = 1
        
        for key,val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))
        
        return [h[1] for h in heap]