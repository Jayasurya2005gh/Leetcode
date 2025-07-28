class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = 0
        sell = 1
        max_profit = 0

        for i in range(1,len(prices)):
            if prices[sell] > prices[buy]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit,max_profit)
            else:
                buy = sell
            sell += 1
        return max_profit
        