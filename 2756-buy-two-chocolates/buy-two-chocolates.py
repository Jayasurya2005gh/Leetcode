class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:

        prices = sorted(prices)

        if len(prices) >= 2:
            curr_money = money
            for i in range(2):
                money -= prices[i]

            if money < 0:
                return curr_money
            else:
                return money
        else:
            for i in prices:
                curr_money = money
                money -= i
    
            if money < 0:
                return curr_money
            else:
                return money
        