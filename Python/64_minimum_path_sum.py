class Solution:
    def minPathSum(self, grid: list[list[int]]) -> int:
        dpTable = [[0] * len(grid[0]) for _ in grid]
            
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if i == 0 and j > 0:
                    dpTable[i][j] = grid[i][j] + dpTable[i][j-1]
                elif j == 0 and i > 0:
                    dpTable[i][j] = grid[i][j] + dpTable[i-1][j]
                elif i == 0 and j == 0:
                    dpTable[i][j] = grid[i][j]
                else:
                    dpTable[i][j] = min(dpTable[i-1][j], dpTable[i][j-1]) + grid[i][j]
                
        return dpTable[-1][-1]
    
    
sol = Solution()
ans = sol.minPathSum([[1]])
print(f'This is the ans: {ans}')