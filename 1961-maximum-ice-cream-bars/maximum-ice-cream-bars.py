class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs = sorted(costs)
        count = 0
        res = coins

        for i in costs:
            if i <= res:
                res -= i
                count += 1
            else:
                break

        return count
        