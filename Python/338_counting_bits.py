class Solution:
        def countBits(self, n: int) -> list[int]:
            ansList = [0]
            if n == 0:
                return ansList
            ansList.append(1)
            if n == 1:
                return ansList
            
            for i in range(2, n+1):
                ansList.append(ansList[i//2] + i % 2)
            return ansList
        
        
        
sol = Solution()
ans = sol.countBits(5)
print(f'This is the ans: {ans}')