class Solution:
    def totalMoney(self, n: int) -> int:

        res = []
        total = 0
        week = 0
        days = 1

        for i in range(n):
            if len(res) == 7:
                total += sum(res)
                res = []
                week += 1
                days = 1
            res.append(week + days)
            days += 1

        if res != []:
            total += sum(res)
            return total
        