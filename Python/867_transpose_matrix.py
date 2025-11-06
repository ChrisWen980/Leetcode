class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        ansMatrix = [['.']*len(matrix) for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                ansMatrix[j][i] = matrix[i][j]
        return ansMatrix
    
sol = Solution()
ans = sol.transpose([[1,2,3],[4,5,6],[7,8,9]])
print(f'This is ans: {ans}')