class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        n = sorted(nums)

        max_1 = n[-1]-1
        max_2 = n[-2]-1

        res = max_1 * max_2
        return res
        