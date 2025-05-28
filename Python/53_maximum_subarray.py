class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        largestSum, currSum = 0, 0
        for i in range(len(nums)):
            if nums[i] > currSum + nums[i]:
                currSum = nums[i]
            else:
                currSum += nums[i]
            largestSum = max(largestSum, currSum)
        return largestSum

sol = Solution()
ans = sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])
print(f'This is the ans: {ans}')