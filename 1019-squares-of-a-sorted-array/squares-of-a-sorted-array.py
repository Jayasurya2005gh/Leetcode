class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        res = []

        for i in nums:
            pos_val = abs(i)
            res.append(pos_val * pos_val)
        return sorted(res)
        