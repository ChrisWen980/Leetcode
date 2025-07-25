from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        uniqueDicts = defaultdict(list)
        for string in strs:
            anagramList = [0] * 26
            for char in string:
                anagramList[ord(char) - ord('a')] += 1
            anagramSig = ' '.join(map(str, anagramList))
            uniqueDicts[anagramSig].append(string)
        sol = list(uniqueDicts.values())
        return sol

sol = Solution()
ans = sol.groupAnagrams(["bdddddddddd","bbbbbbbbbbc"])
print(f'This is the ans: {ans}')