class Solution:
    def countSquares(self, matrix: list[list[int]]) -> int:
        dpTable = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        totalSquares = 0
        for n in range(len(matrix)):
            for m in range(len(matrix[0])):
                if matrix[n][m] == 0:
                    dpTable[n][m] = 0
                elif n == 0 or m == 0: # base case
                    dpTable[n][m] = 1
                else:
                    dpTable[n][m] = min(dpTable[n-1][m], dpTable[n][m-1], dpTable[n-1][m-1]) + 1
                totalSquares += dpTable[n][m]
        print(dpTable)
        return totalSquares
    
sol = Solution()
ans = sol.countSquares([
  [0,1,1,1],
  [1,1,1,1],
  [0,1,1,1]
])
print(f'This is ans: {ans}')