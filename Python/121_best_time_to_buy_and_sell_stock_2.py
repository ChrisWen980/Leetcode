class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        currBuy, profit = prices[0], 0
        
        for i in range(1, len(prices)):
            if prices[i] < currBuy:
                currBuy = prices[i]
            profit = max(prices[i] - currBuy, profit)
        return profit

sol = Solution()
maxProf = sol.maxProfit([7,1,5,3,6,4])
print(f'This is maxProf: {maxProf}')