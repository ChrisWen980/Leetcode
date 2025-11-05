matrix = [[1,2,3],[4,5,6],[7,8,9]]
class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for y in range(n//2):
            for x in range(n - n//2):
                print(y, x)
                matrix[y][x], matrix[x][~y], matrix[~y][~x], matrix[~x][y] =\
                    matrix[~x][y], matrix[y][x], matrix[x][~y], matrix[~y][~x]
        
sol = Solution()
sol.rotate(matrix)
print(f'This is ans: {matrix}')