class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = set()

        for i in permutations(nums):
            res.add(i)

        return list(res)