class Solution:
    def countSubstrings(self, s: str) -> int:
        def findPalindromes(s: str, L: int, R: int):
            palins = 0
            while (L >= 0 and R < len(s)) and s[L] == s[R]:
                palins += 1
                L -= 1
                R += 1
            return palins
        
        totalPalins = 0
        for i in range(len(s)):
            totalPalins += findPalindromes(s, i, i) + findPalindromes(s, i, i+1)
        return totalPalins
    
sol = Solution()
ans = sol.countSubstrings('cbbd')
print(f'This is the ans: {ans}')