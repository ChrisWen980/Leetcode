import re
import math

class Solution:
    def isPalindrome(self, s: str) -> bool:
        stripS = re.sub(r'[^a-zA-Z0-9]+', '', s)
        order = []
        
        for i in range(len(stripS)//2):
            order.append(stripS[i])  
        for i in range(math.ceil(len(stripS)/2), len(stripS)):
            if stripS[i].lower() != order.pop().lower():
                return False
        return True
        

sol = Solution()
ans = sol.isPalindrome('A man, a plan, a canal: Panama')
print(f'This is the ans: {ans}')