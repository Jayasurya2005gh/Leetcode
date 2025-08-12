class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        sort = sorted(nums)
        total_len = len(sort)
        mid_element = total_len // 2
        return sort[mid_element]
        