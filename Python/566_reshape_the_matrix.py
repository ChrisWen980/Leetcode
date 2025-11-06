class Solution:
    def matrixReshape(self, mat: list[list[int]], r: int, c: int) -> list[list[int]]:
        rows, cols = len(mat), len(mat[0])
        if rows*cols != r*c:
            return mat

        ansMat = [['.']*c for _ in range(r)]
        #print(ansMat)
        xPtr, yPtr = 0, 0
        for y in range(rows):
            for x in range(cols):
                #print(y, x)
                ansMat[yPtr][xPtr] = mat[y][x]
                if xPtr < c-1:
                    xPtr += 1
                else:
                    yPtr += 1
                    xPtr = 0
        return ansMat
    
sol = Solution()
ans = sol.matrixReshape([[1,2,3],[4,5,6]], 3, 2)
print(f'This is ans: {ans}')