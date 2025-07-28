class Solution:
    def reverse(self, x: int) -> int:
        sign = 1
        if x < 0:
            sign = -1
            x *= -1
        
        strX = str(x)
        reversedX = int(strX[::-1]) * sign
        if reversedX < -(2**31) or reversedX > (2**31) - 1:
            return 0
        return reversedX
    
sol = Solution()
ans = sol.reverse(-123)
print(f'This is the ans: {ans}')