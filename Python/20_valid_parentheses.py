class Solution:
    def isValid(self, s: str) -> bool:
        orderList = []
        charMap = {'(':')', '{':'}', '[':']'}
        for char in s:
            if char in charMap:
                orderList.append(char)
            elif len(orderList) == 0:
                return False
            else:
                if char != charMap[orderList.pop()]:
                    return False
        return True if len(orderList) == 0 else False
    
sol = Solution()
ans = sol.isValid('()[]{}')
print(f'This is the ans: {ans}')