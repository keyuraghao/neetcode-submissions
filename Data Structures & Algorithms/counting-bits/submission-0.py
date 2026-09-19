class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n+1)

        for i in range(32):
            mask = 1 << i
            if mask > n:
                break
            for j in range(mask,n+1):
                if j & mask:
                    result[j] += 1
        return result
