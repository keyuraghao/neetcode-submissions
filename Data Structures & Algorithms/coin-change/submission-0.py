class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount+1)
        dp[0] = 0

        for a in range(1,amount+1):
            for c in coins:
                if a-c >= 0: # this condition checks that if amount - value of curr coin > 0
                    dp[a] = min(dp[a],1+dp[a-c]) # this is amount of coins required to make 'a'. lets say we already have computed the dp[a] but we need the min coins so 1+dp[a-c] here '1' is the coin that we are considering and c is the value of it (ex. the total amount needed is 7 i.e 'a = 7' and we have coins [1,3,4,5] so when we consider a coin 3 we are counting it as 1 + no.of coins needed for (7-3)->(4))
        
        return dp[amount] if dp[amount] != amount + 1 else -1