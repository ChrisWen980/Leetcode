class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {1:1, 2:2}
        if n in dp:
            return dp[n]
        for i in range(2, n):
            dp[i+1] = dp[i-1] + dp[i] 
        return dp[n]
        

sol = Solution()
ans = sol.climbStairs(5)
print(f'This is the ans: {ans}')