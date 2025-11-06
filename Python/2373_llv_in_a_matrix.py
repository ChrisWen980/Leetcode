class Solution:
    def largestLocal(self, grid: list[list[int]]) -> list[list[int]]:
        rows = len(grid)
        ansMatrix = [['.']*(rows-2) for _ in range(rows-2)]
        for i in range(1, rows-1):
            for j in range(1, rows-1):
                ansMatrix[i-1][j-1] = max(grid[i-1][j-1:j+2]+grid[i][j-1:j+2]+grid[i+1][j-1:j+2])
        return ansMatrix
    
sol = Solution()
ans = sol.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
print(f'This is ans: {ans}')