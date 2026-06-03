class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        max_profit = 0

        for i in prices:
            if i < buy:
                buy = i

            profit = i - buy
            if profit > max_profit:
                max_profit = profit
        return max_profit
        