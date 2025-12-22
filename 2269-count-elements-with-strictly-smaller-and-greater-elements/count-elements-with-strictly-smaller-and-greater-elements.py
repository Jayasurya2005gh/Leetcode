class Solution:
    def countElements(self, nums: List[int]) -> int:

        nums = sorted(nums)
        max_num = max(nums)
        min_num = min(nums)
        count = 0

        for i in nums:
            if i < max_num and i > min_num:
                count += 1
        return count

        