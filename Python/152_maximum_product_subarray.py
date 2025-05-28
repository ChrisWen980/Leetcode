class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        minProd, maxProd = 1, 1
        ans = max(nums)
        
        for i in range(len(nums)):
            temp = maxProd * nums[i]
            maxProd = max(temp, minProd * nums[i], nums[i])
            minProd = min(temp, minProd * nums[i], nums[i])
            ans = max(maxProd, ans)
        return ans
    
    
sol = Solution()
ans = sol.maxProduct([2,3,-2,4])
print(f'This is the ans: {ans}')