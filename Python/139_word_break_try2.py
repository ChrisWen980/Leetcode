# https://leetcode.com/problems/word-break/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dpList = [False for _ in range(len(s) + 1)]
        dpList[0] = True
        
        for i in range(len(dpList)):
            for word in wordDict:
                if i - len(word) < 0:
                    continue
                if dpList[i - len(word)] == True and s[i - len(word):i] == word:
                    dpList[i] = True
                    continue
                    
        return dpList[-1]
        
sol = Solution()
ans = sol.wordBreak(s = "applepenapple", wordDict = ["apple","pen"])
print(f'This is the ans: {ans}')