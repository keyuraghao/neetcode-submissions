class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # bruteforce solution ( this is bad as the time complexity is O(n^2))
        # maxx = 0

        # for left in range(len(heights)):
        #     for right in range(left + 1, len(heights)):
        #         area = (right - left) * min(heights[right], heights[left])
        #         maxx = max(maxx, area)
        # return maxx


        max_area = 0

        left = 0 
        right = len(heights) - 1

        while left < right:
            area = (right - left) * min(heights[left], heights[right])
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area