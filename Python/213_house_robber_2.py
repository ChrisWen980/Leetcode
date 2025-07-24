class Solution:
    def rob(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        elif len(nums) == 3:
            return max(nums[0], max(nums[1], nums[2]))
        
        def simpleRob(nums: list[int]) -> int:
            dp = [0] * len(nums)
            for i in range(len(nums)):
                dp[i] = max(nums[i] + dp[i-2], dp[i-1])
            print(f'This is dp: {dp}')
            return dp[-1]
          
        return max(simpleRob(nums[0:len(nums)-1]), simpleRob(nums[1:len(nums)]))
        
sol = Solution()
ans = sol.rob([1, 2, 3, 1])
print(f'This is the ans: {ans}')