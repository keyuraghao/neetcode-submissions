class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        minn = 1
        maxx = max(piles)
        ans = maxx
        while minn <= maxx:
            mid = (minn + maxx) // 2
            curr_time = 0
            for val in piles:
                curr_time += math.ceil(val / mid)
            if curr_time > h:
                minn = mid + 1
            elif curr_time <= h:
                maxx = mid - 1
                ans = mid
        return ans