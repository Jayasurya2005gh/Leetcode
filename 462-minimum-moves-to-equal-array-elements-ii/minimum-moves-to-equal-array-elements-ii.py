class Solution:
    def minMoves2(self, nums: List[int]) -> int:

        nums = sorted(nums)
        nums_len = len(nums)
        mid_num = nums[nums_len // 2]
        res = 0

        for i in nums:
            res += abs(i - mid_num)
        return res

        