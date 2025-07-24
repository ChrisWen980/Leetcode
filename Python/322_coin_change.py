class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        dp = [amount+1] * (amount+1)
        dp[0] = 0
        for i in range(1,amount+1):
            for coin in coins:
                if coin > i:
                    continue
                elif coin == i:
                    dp[i] = 1
                else:
                    dp[i] = min(dp[i-coin]+1, dp[i])
        if dp[amount] <= amount:
            return dp[amount] 
        return -1
    
sol = Solution()
ans = sol.coinChange([1, 2, 5], 11)
print(f'This is the ans: {ans}')