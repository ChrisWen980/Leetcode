class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        maxInt = 2**31 - 1
        
        while b != 0:
            sum = (a ^ b) & mask
            carry = (a & b) & mask
            
            a = sum
            b = carry << 1
        
        return a if a <= maxInt else ~(a ^ mask)
    
sol = Solution()
ans = sol.getSum(-4, 10)
print(f'This is the ans: {ans}')