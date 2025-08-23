class Solution:
    def largestAltitude(self, gain: List[int]) -> int:

        res = [0]
        curr_sum = 0

        for i in gain:
            curr_sum += i
            res.append(curr_sum)
        return max(res)
        