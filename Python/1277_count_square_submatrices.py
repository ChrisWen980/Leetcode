class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dpTable = [[0] * (n+1) for _ in range(m+1)]
        ans = 0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]:
                    dpTable[i+1][j+1] = min(dpTable[i][j], dpTable[i+1][j], dpTable[i][j+1]) + 1
                    ans += dpTable[i+1][j+1]  
        return ans
    
sol = Solution()
ans = sol.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])
print(f'This is ans: {ans}')