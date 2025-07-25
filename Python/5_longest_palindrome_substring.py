class Solution:
    def longestPalindrome(self, s: str) -> str:
        def findLongestPalindrome(s: str, L: int, R: int):
            while (L >= 0 and R < len(s)) and s[L] == s[R]:
                L -= 1
                R += 1
            return s[L+1:R]
        
        longestStr = ''
        for i in range(len(s)):
            longestStr = max(findLongestPalindrome(s, i, i), findLongestPalindrome(s, i, i+1), longestStr, key=len)
        
        return longestStr

sol = Solution()
ans = sol.longestPalindrome('cbbd')
print(f'This is the ans: {ans}')