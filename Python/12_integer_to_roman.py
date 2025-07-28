class Solution:
    def intToRoman(self, num: int) -> str:
        rNumMap = {
            1000:'M',
            900:'CM',
            500:'D',
            400:'CD',
            100:'C',
            90:'XC',
            50:'L',
            40:'XL',
            10:'X',
            9:'IX',
            5:'V',
            4:'IV',
            1:'I'
        }
        
        romStr = ''
        for key in rNumMap:
            if key <= num:
                romStr += rNumMap[key] * (num//key)
                num = num % key
        return romStr
    
    
sol = Solution()
ans = sol.intToRoman(58)
print(f'This is the ans: {ans}')