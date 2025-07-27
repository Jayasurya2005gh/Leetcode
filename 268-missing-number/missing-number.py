class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        n = set(nums)
        res = 0
        for i in range(1,len(nums)+1):
            if i not in n:
                res = i
        return res


        