class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        wordDict = {}
        for char in s:
            if char not in wordDict:
                wordDict[char] = 0
            wordDict[char] += 1
        
        for char in t:
            if char not in wordDict:
                return False
            wordDict[char] -= 1
        
        return True if max(wordDict.values()) == 0 else False
        
sol = Solution()
ans = sol.isAnagram('anagram', 'nagaram')
print(f'This is the ans: {ans}')