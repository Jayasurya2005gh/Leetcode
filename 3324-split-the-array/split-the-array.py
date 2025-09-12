class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        set_nums = list(set(nums))

        for i in set_nums:
            if nums.count(i) <= 2:
                continue
            else:
                return False
        return True
        