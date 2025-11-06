class Solution:
    def findDiagonalOrder(self, mat: list[list[int]]) -> list[int]:
        ansDict = {}
        for y in range(len(mat)):
            for x in range(len(mat[y])):
                #print(mat[y][x])
                if x+y not in ansDict:
                    ansDict[x+y] = [mat[y][x]]
                else:
                    ansDict[x+y].append(mat[y][x])
        ansList = []        
        for key in ansDict:
            if key % 2 == 0:
                ansList += ansDict[key][::-1]
            else:
                ansList += ansDict[key]
        return ansList
    
sol = Solution()
ans = sol.findDiagonalOrder([[1,2,3],[4,5,6],[7,8,9]])
print(f'This is ans: {ans}')