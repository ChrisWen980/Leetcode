class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        res = [1] * len(nums)
        
        curr = 1
        for i in range(len(nums)):
            res[i] *= curr
            curr *= nums[i]
        
        curr = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= curr
            curr *= nums[i]
        
        return res
            
sol = Solution()
result = sol.productExceptSelf([1, 2, 3, 4])
print(f'This is result: {result}')