class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        result = [1] * len(nums)
        for i in range(1, len(nums)):
            result[i] = result[i-1] * nums[i-1]
            
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]
        return result
            
sol = Solution()
result = sol.productExceptSelf([1, 2, 3, 4])
print(f'This is result: {result}')