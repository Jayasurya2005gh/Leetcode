class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:

        if len(nums) == 1:
            if nums[0] == k:
                return k * 2

        for i in range(1, len(nums) + 1):
            if k * i in nums:
                continue
            else:
                return k * i
        return nums[len(nums) - 1] + k
        