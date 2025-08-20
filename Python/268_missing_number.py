class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)
        
        for i in range(1, n+1):
            ans ^= i
        for i in range(0, n):
            ans ^= nums[i]
            
        return ans
        
        
        
sol = Solution()
ans = sol.missingNumber([3,0,1])
print(f'This is the ans: {ans}')