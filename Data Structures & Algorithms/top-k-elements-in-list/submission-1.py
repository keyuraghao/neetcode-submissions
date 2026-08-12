import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # This problem can be solved in 2 different ways 
        # 1. using the bucket sort Time : O(n)
        # 2. using the heap Time O(klogn)

        # doing with the bucket sort
        # count = {}
        # freq = [[] for i in range(len(nums)+1)]

        # for i in nums:
        #     if i in count:
        #         count[i] += 1
        #     else:
        #         count[i] = 1
        
        # for key,val in count.items():
        #     freq[val].append(key)
        
        # ans = []

        # for i in range(len(freq)-1,0,-1):
        #     for n in freq[i]:
        #         ans.append(n)
        #         if len(ans) == k:
        #             return ans

        # runtime 301 ms

        # now using the heap (heapify)

        counter = {}
        heap = []
        for i in nums:
            if i in counter:
                counter[i] += 1
            else:
                counter[i] = 1
        
        for key,val in counter.items():
            if len(heap) < k:
                heapq.heappush(heap,(val,key))
            else:
                heapq.heappushpop(heap,(val,key))

        return [h[1] for h in heap]


