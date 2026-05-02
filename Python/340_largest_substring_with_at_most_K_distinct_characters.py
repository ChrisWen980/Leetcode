from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        substrDict = defaultdict(int)
        start = 0
        maxsubstr = 0
        
        for end in range(len(s)):
            substrDict[s[end]] += 1
            
            while len(substrDict) > k:
                substrDict[s[start]] -= 1
                if substrDict[s[start]] == 0:
                    del substrDict[s[start]]
                start += 1
            
            maxsubstr = max(maxsubstr, end - start + 1)
        return maxsubstr
    
sol = Solution()
ans = sol.lengthOfLongestSubstringKDistinct("eceba", 2)
print(f'This is the ans: {ans}')