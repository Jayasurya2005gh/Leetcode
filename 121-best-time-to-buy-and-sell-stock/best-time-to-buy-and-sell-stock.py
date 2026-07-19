class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        buy = prices[0]
        max_profit = 0

        for i in prices:
            if i < buy:
                buy = i

            curr_profit = (i - buy)
            if curr_profit > max_profit:
                max_profit = curr_profit
        return max_profit
        