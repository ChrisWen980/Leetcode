class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        phoneMap = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        
        combs = []
        
        def recursion(comb, nextDigits):
            #print(f'combs: {combs}, comb: {comb}, nextDigits: {nextDigits}')
            for i in range(len(phoneMap[nextDigits[0]])):
                if len(nextDigits) == 1:
                    combs.append(comb + phoneMap[nextDigits[0]][i])
                else:
                    recursion(comb + phoneMap[nextDigits[0]][i], nextDigits[1:])
            
        if len(digits) > 0:
            recursion('', digits)
        #print(combs)
        return combs
 
 
sol = Solution()
ans = sol.letterCombinations('23')
print(f'This is the ans: {ans}')