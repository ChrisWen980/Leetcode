class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tDict = {}
        for char in t:
            if char not in tDict:
                tDict[char] = 0
            tDict[char] += 1
        
        minSSCount, leftP = len(s)+1, 0
        minSS = ''
        for rightP in range(len(s)):
            print(f'leftP: {leftP}, rightP: {rightP}, min: {minSS}, tDict: {tDict}')
            if s[rightP] in tDict:
                tDict[s[rightP]] -= 1
            while max(tDict.values()) <= 0 and leftP <= rightP:
                if rightP-leftP+1 <= minSSCount:
                    minSSCount = rightP-leftP+1
                    minSS = s[leftP:rightP+1]
                if s[leftP] in tDict:
                    tDict[s[leftP]] += 1
                leftP += 1
                print(f'leftP: {leftP}, tDict: {tDict}')
        return minSS
    
sol = Solution()
ans = sol.minWindow('ADOBECODEBANC', 'ABC')
print(f'This is the ans: {ans}')