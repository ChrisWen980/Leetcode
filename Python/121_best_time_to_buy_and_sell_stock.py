class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
            elif prices[i] - buy > profit:
                profit = prices[i] - buy
        return profit
        
sol = Solution()
maxProf = sol.maxProfit([7,1,5,3,6,4])
print(f'This is maxProf: {maxProf}')