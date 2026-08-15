
class MedianFinder:
    # implement using 2 heaps (large and small)
    # small heap --> max heap
    # large heap --> min heap
    # this structure because to find the median we need the max value from the small heap and the min value from the large heap 

    def __init__(self):
        self.small = []
        self.large = []        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small,num * (-1)) # max heap

        if (self.small and self.large and ((-1)*self.small[0]) > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)        

        # abs(len(small) - len(large)) > 2
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large,val)
        if len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small,-1*val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        return ((-1*self.small[0]) + self.large[0]) / 2
        