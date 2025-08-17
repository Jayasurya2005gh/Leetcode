class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        g = 0
        p = 0

        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            p += gas[i] - cost[i]
            if p < 0:
                p = 0
                g = i + 1
        return g
        