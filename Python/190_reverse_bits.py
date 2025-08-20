class Solution:
    def reverseBits(self, n: int) -> int:
        binaryN = bin(n)[2:]
        missingZeros = '0' * (32-len(binaryN)) + binaryN
        return int(missingZeros[::-1], 2)
        
        
        
sol = Solution()
ans = sol.reverseBits(43261596)
print(f'This is the ans: {ans}')