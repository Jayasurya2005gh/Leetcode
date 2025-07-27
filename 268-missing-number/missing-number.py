class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = 0
        for i in range(1,len(nums)+1):
            if i not in nums:
                res = i
        return res


        