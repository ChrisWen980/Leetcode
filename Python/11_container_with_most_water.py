class Solution:
    def maxArea(self, height: list[int]) -> int:
        L, R, largestArea = 0, len(height)-1, 0
         
        while L < R:
            largestArea = max(largestArea, min(height[L], height[R]) * (R-L))
            if height[L] < height[R]:
                L += 1
            elif height[L] > height[R]:
                R -= 1
            else:
                if height[L+1] >= height[R-1]:
                    L += 1
                else:
                    R -= 1
        
        return largestArea    
        

sol = Solution()
ans = sol.maxArea([1,8,6,2,5,4,8,3,7])
print(f'This is the ans: {ans}')