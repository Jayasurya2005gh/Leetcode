class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:

        res = []
        set_nums = list(set(nums))

        for i in set_nums:
            if nums.count(i) <= 2:
                res.append(i)
            else:
                return False
        return True
        