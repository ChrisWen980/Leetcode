# https://leetcode.com/problems/word-break-ii/description/

class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> list[str]:
        wordSet = set(wordDict)
        
        # Recursive function
        def exploreSubstring(substr):
            # Possibly combinations for substr
            combs = []
            
            # If substr was completed return empty
            if not substr:
                return [""]
            
            # Iterate through substr to see if this starting word exists
            for i, _ in enumerate(substr):
                word = substr[:i+1]
                
                # If it does extend it and try to explore for possible words after
                if word in wordSet:
                    # f'{word} {sentence}' builds out the sentence then extends it into the list if sentence exists
                    combs.extend([f'{word} {sentence}' if sentence else word for sentence in exploreSubstring(substr[i+1:])])
            
            return combs
    
        return exploreSubstring(s)
    
sol = Solution()
ans = sol.wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"])
print(f'This is the ans: {ans}')