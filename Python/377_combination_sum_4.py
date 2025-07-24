class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        dp = [0] * (target+1)
        
        for i in range(len(dp)):
            for j in range(len(nums)):
                if i - nums[j] < 0:
                    continue
                elif i - nums[j] == 0:
                    dp[i] += 1
                else:
                    dp[i] += dp[i-nums[j]]        
        return dp[target]
        
sol = Solution()
ans = sol.combinationSum4([1,2,3], 4)
print(f'This is the ans: {ans}')