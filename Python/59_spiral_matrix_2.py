class Solution:
    def generateMatrix(self, n: int) -> list[list[int]]:
        x, y, dx, dy = 0, 0, 1, 0
        ans = [[0]*n for i in range(n)]
        #print(ans)

        for num in range(1, n*n+1):
            #print(f'This is ans: {ans}, and this is x: {x} and y: {y}')
            ans[y][x] = num

            if not 0 <= x+dx < n or not 0 <= y+dy < n or ans[y+dy][x+dx] != 0:
                dx, dy = -dy, dx
            
            x += dx
            y += dy
        return ans
        
sol = Solution()
ans = sol.generateMatrix(3)
print(f'This is ans: {ans}')