class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:

        res = []
        total = 0

        for i in range(numOnes):
            res.append(1)
        for i in range(numZeros):
            res.append(0)
        for i in range(numNegOnes):
            res.append(-1)

        res = sorted(res)
        res = res[::-1]

        for i in range(k):
            total += res[i]
        return total
        