class Solution:
    def rob(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(len(nums)):
            if i - 2 < 0:
                dp[i] = max(dp[i-1], nums[i])
            else:
                dp[i] = max(dp[i-1], dp[i-2]+nums[i])        
        return dp[-1]
        
sol = Solution()
ans = sol.rob([2,7,9,3,1])
print(f'This is the ans: {ans}')