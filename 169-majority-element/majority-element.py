class Solution:
    def majorityElement(self, nums: List[int]) -> int:


        sort = sorted(nums)
        mid_element = len(sort) // 2
        return sort[mid_element]
        