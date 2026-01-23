class Solution:
    def getSum(self, a: int, b: int) -> int:
        mask = 0xFFFFFFFF
        
        # python is 64 bit but in this scenario we only care about 32
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry
                
        return a & mask if b > 0 else a
    
sol = Solution()
ans = sol.getSum(-4, 10)
print(f'This is the ans: {ans}')