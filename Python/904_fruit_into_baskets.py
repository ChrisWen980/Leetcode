from collections import defaultdict

class Solution:
    def totalFruit(self, fruits: list[int]) -> int:
        maxFruits, start = 0, 0
        fruitsDict = defaultdict(int)
        
        for end in range(len(fruits)):
            fruitsDict[fruits[end]] += 1
            while len(fruitsDict) > 2:
                fruitsDict[fruits[start]] -= 1
                if fruitsDict[fruits[start]] == 0:
                    del fruitsDict[fruits[start]]
                start += 1
            maxFruits = max(maxFruits, end - start + 1)
            print(f'maxFruits: {maxFruits}')
            print(fruitsDict)
        return maxFruits
    
    
sol = Solution()
ans = sol.totalFruit([3,3,3,1,2,1,1,2,3,3,4]) # ans = 5
print(f'This is ans: {ans}')