class Solution:
    def fullJustify(self, words: list[str], maxWidth: int) -> list[str]:
        strAns, curr, letterCount = [], [], 0
        for word in words:
            if letterCount + len(word) + len(curr) > maxWidth:
                for i in range(maxWidth - letterCount):
                    curr[i%(len(curr) or 0)] += ' '
                strAns.append(''.join(curr))
                curr, letterCount = [], 0
            letterCount += len(word)
            curr += [word]
        return strAns + [' '.join(curr).ljust(maxWidth)]
    
sol = Solution()
ans = sol.fullJustify(["This", "is", "an", "example", "of", "text", "justification."], 16)
print(f'This is the ans: {ans}')