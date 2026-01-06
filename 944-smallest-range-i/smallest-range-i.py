class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:

        ans = 2 * k

        if (max(nums) - min(nums)) - ans <= 0:
            return 0
        else:
            res = (max(nums) - min(nums)) - ans
            return res
        