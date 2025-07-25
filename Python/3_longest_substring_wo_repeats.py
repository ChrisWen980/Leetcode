class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        
        charMap = {}
        leftPointer, longestString = 0, 0
        for rightPointer in range(len(s)):
            if s[rightPointer] in charMap and charMap[s[rightPointer]] >= leftPointer:
                longestString = max(longestString, rightPointer-leftPointer)
                leftPointer = charMap[s[rightPointer]]+1
                charMap[s[rightPointer]] = rightPointer
            else:
                charMap[s[rightPointer]] = rightPointer
        return max(longestString, rightPointer-leftPointer+1)
        
sol = Solution()
ans = sol.lengthOfLongestSubstring('bbbb')
print(f'This is the ans: {ans}')