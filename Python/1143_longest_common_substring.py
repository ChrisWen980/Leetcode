class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dpTable = [[0] * (len(text2) + 1) for _ in range(len(text1) + 1)]
        for i in range(len(text1)-1, -1, -1):
            for j in range(len(text2)-1, -1, -1):
                if text1[i] == text2[j]:
                    dpTable[i][j] = dpTable[i+1][j+1] + 1
                else:
                    dpTable[i][j] = max(dpTable[i+1][j], dpTable[i][j+1])
        return dpTable[0][0]
        
sol = Solution()
ans = sol.longestCommonSubsequence('abcde', 'ace')
print(f'This is the ans: {ans}')