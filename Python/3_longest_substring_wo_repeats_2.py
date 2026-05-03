class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        words = set()
        leftP, maxLen = 0, 0
        for char in s:
            while char in words:
                words.remove(s[leftP])
                leftP += 1        
            words.add(char)
            maxLen = max(maxLen, len(words))
        return maxLen
        
sol = Solution()
ans = sol.lengthOfLongestSubstring('bbbb')
print(f'This is the ans: {ans}')