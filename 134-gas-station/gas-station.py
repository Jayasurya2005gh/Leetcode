class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        g = 0
        t = 0
        if sum(gas) < sum(cost):
            return -1

        for i in range(len(gas)):
            t += gas[i]
            t -= cost[i]

            if t < 0:
                t = 0
                g = i+1
        return g

        
        