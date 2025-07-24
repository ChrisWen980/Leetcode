class Solution:
    def numDecodings(self, s: str) -> int:
        if int(s) == 0 or s[0] == '0':
            return 0
        dpList = [0] * (len(s)+1)
        dpList[0] = 1
        dpList[1] = 1
        for i in range(2, len(s)+1):
            if int(s[i-1]) > 0:
                dpList[i] += dpList[i-1]
            
            if 10 <= int(s[i-2:i]) <= 26:
                dpList[i] += dpList[i-2]
        return dpList[-1]
        
        
sol = Solution()
ans = sol.numDecodings('2202')
print(f'This is the ans: {ans}')