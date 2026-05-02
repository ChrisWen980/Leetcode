class Solution:
    def rob(self, nums: list[int]) -> int:
        # base cases
        if 1 <= len(nums) <= 3:
            return max(nums)
        
        def rob_houses(subNums: list[int]):
            dpTable = [0 for _ in range(len(subNums))]
            dpTable[0] = subNums[0]
            dpTable[1] = max(dpTable[0], subNums[1])
            
            for i in range(2, len(subNums)):
                dpTable[i] = max(dpTable[i-2] + subNums[i], dpTable[i-1])
            return dpTable[-1]
        
        return max(rob_houses(nums[0:len(nums)-1]), rob_houses(nums[1:len(nums)]))
            
        
sol = Solution()
ans = sol.rob([1, 5, 3, 6])
print(f'This is the ans: {ans}')