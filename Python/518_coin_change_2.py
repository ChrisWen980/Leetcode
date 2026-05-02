class Solution:
    def change(self, amount: int, coins: list[int]) -> int:
        dpTable = [0 for _ in range(amount+1)]
        dpTable[0] = 1  # base case for no coins needed to make total of 0
        for coin in coins:
            for i in range(coin, amount+1):
                dpTable[i] += dpTable[i-coin]
        return dpTable[-1]
    
sol = Solution()
ans = sol.change(amount = 5, coins = [1,2,5])
print(f'This is ans: {ans}')