class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        maxSum, dpTable = nums[0], [0] * len(nums)
        dpTable[0] = nums[0]
        
        for i in range(1, len(nums)):
            if dpTable[i-1] > 0:
                dpTable[i] = dpTable[i-1] + nums[i]
            else:
                dpTable[i] = nums[i]
            maxSum = max(maxSum, dpTable[i])
        return maxSum
        
sol = Solution()
ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(f'This is the ans: {ans}')