class Solution:
        def hammingWeight(self, n: int) -> int:
            res = 0
            for i in range(32):
                res += (n >> i) & 1
            return res
        
sol = Solution()
ans = sol.hammingWeight(2147483645)
print(f'This is the ans: {ans}')