class Solution:
    def maximumProduct(self, nums: List[int]) -> int:

        nums = sorted(nums)
        res = max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])
        return res
        