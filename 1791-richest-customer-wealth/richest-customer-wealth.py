class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:

        res = []

        for i in accounts:
            total_val = sum(i)
            if total_val not in res:
                res.append(total_val)

        return max(res)        