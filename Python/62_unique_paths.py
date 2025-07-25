class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        dpTable = [[1] * n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dpTable[i][j] = dpTable[i-1][j] + dpTable[i][j-1]
        
        return dpTable[-1][-1]
        
sol = Solution()
ans = sol.uniquePaths(2, 2)
print(f'This is the ans: {ans}')