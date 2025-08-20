class Solution:
        def hammingWeight(self, n: int) -> int:
            return bin(n).count('1', 2)
        
        
        
sol = Solution()
ans = sol.hammingWeight(2147483645)
print(f'This is the ans: {ans}')