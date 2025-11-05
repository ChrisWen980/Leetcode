class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        x, y, dx, dy = 0, 0, 1, 0
        rows, cols = len(matrix), len(matrix[0])
        ans = []

        for num in range(rows * cols):
            ans.append(matrix[y][x])
            matrix[y][x] = '.'

            if not 0 <= x+dx < cols or not 0 <= y+dy < rows or matrix[y+dy][x+dx] == '.':
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        return ans
        
sol = Solution()
ans = sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
print(f'This is ans: {ans}')