class Solution:
    def maximizeExpressionOfThree(self, nums: List[int]) -> int:

        ans = sorted(nums)
        a = ans[-1]
        b = ans[-2]
        c = ans[0]

        res = a + b - (c)
        return res
        