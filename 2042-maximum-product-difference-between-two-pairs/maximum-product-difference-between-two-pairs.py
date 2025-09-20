class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:

        nums = sorted(nums)
        res = nums[0] * nums[1] - nums[-1] * nums[-2]
        return abs(res)