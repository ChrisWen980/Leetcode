class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        maxProd, minProd, ans = 1, 1, nums[0]
        
        for i in range(len(nums)):
            tempMax = maxProd
            maxProd = max(tempMax * nums[i], minProd * nums[i], nums[i])
            minProd = min(tempMax * nums[i], minProd * nums[i], nums[i])
            ans = max(maxProd, minProd, ans)
            
        return ans
        
    
    
sol = Solution()
ans = sol.maxProduct([2,3,-2,4])
print(f'This is the ans: {ans}')