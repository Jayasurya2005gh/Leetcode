class Solution:
    def dominantIndex(self, nums: List[int]) -> int:

        n = sorted(nums)

        if n[-2] * 2 <= n[-1]:
            return nums.index(max(n))
        else:
            return -1
        