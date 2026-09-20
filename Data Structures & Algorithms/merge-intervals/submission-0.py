class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x : x[0])
        ans = [intervals[0]]

        for start, end in intervals[1:]:
            last = ans[-1][1]

            if start <= last:
                ans[-1][1] = max(last,end)
            else:
                ans.append([start,end])
        return ans