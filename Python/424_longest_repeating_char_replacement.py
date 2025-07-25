class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freqDict = {s[0]:1}
        longest, rightP, leftP = 0, 0, 0
        for rightP in range(1, len(s)):
            #print(f'leftP: {leftP}, rightP: {rightP}')
            if s[rightP] in freqDict:
                freqDict[s[rightP]] += 1
            else:
                freqDict[s[rightP]] = 1
            #print(freqDict)
                
            if rightP-leftP+1-max(freqDict.values()) > k:
                longest = max(longest, rightP-leftP)
                #print(f'longest: {longest}')
                while rightP-leftP+1-max(freqDict.values()) > k:
                    freqDict[s[leftP]] -= 1
                    leftP += 1
                    #print(f'leftP: {leftP}')
                
        return max(longest, rightP-leftP+1)
        

sol = Solution()
ans = sol.characterReplacement('ABBB', 2)
print(f'This is the ans: {ans}')