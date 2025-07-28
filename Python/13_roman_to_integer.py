class Solution:
    def romanToInt(self, s: str) -> int:
        rNumMap = {
            'M':1000,
            'CM':900,
            'D':500,
            'CD':400,
            'C':100,
            'XC':90,
            'L':50,
            'XL':40,
            'X':10,
            'IX':9,
            'V':5,
            'IV':4,
            'I':1
        }
        
        romInt = 0
        endPtr = len(s)-1
        for pos in range(len(s)):
            if pos+1 <= endPtr and rNumMap[s[pos]] < rNumMap[s[pos+1]]:
                romInt -= rNumMap[s[pos]]
            else:
                romInt += rNumMap[s[pos]]
        return romInt
    
    
sol = Solution()
ans = sol.romanToInt('LVIII')
print(f'This is the ans: {ans}')