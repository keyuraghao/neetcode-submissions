class Solution:
    def climbStairs(self, n: int) -> int:
        # solution 1 using only 2 variables Time O(n) Space O(1)
        one , two = 1,1
        for i in range(n-1):
            temp = one
            one = one + two
            two = temp
        return one


        