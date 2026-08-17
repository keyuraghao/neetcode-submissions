class Solution:
    def climbStairs(self, n: int) -> int:
        # solution using the Cache
        # Time O(n) Space O(n)
        cache = {}

        def climb(i):
            if i == 0:
                return 1
            if i < 0:
                return 0
            if i in cache:
                return cache[i]

            cache[i] = climb(i-1) + climb(i-2)
            return cache[i]

        return climb(n)