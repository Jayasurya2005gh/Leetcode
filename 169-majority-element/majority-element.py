class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        nums = sorted(nums)
        mid_part = len(nums) // 2
        return nums[mid_part]
        