class Solution:
    def maximumGap(self, nums: List[int]) -> int:

        l = 0
        max_total = 0
        nums = sorted(nums)

        if len(nums) < 2:
            return 0
        for r in range(1,len(nums)):
            total = nums[r] - nums[l]
            max_total = max(max_total,total)
            l += 1
        return abs(max_total)

        