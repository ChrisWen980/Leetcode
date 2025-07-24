class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        dpList = [False] * (len(s)+1)
        dpList[0] = True
        
        for i in range(len(dpList)):
            for j in range(len(wordDict)):
                if i - len(wordDict[j]) < 0:
                    continue
                elif dpList[i - len(wordDict[j])] == True and s[i-len(wordDict[j]):i] == wordDict[j]:
                    dpList[i] = True
        print(dpList)
        return dpList[-1]
        
sol = Solution()
ans = sol.wordBreak("applepenapple", ["apple","pen"])
print(f'This is the ans: {ans}')