class Solution:
    def minOperations(self, nums: list[int], x: int) -> int:
        minOpers, leftP, rightP = float('inf'), 0, len(nums)-1
        
        while x > 0:
            x -= nums[leftP]
            leftP += 1
            
            if leftP > rightP and x > 0:
                return -1
            elif x == 0:
                minOpers = leftP
        
        
        while leftP >= 0:
            leftP -= 1
            x += nums[leftP]
            
            
            while x > 0:
                x -= nums[rightP]
                rightP -= 1
                
            if x == 0:
                minOpers = min(minOpers, leftP + (len(nums) - 1 - rightP))
        
        return -1 if minOpers == float('inf') else minOpers
    
    
sol = Solution()
ans = sol.minOperations(nums = [1,1,4,2,3], x = 5)   # 5
print(f'This is the ans: {ans}')