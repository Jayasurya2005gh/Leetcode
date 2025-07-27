class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        res = 0
        ans = []
        for i in range(1,len(nums)+1):
            if i in nums:
                ans.append(i)
            else:
                res = i
        return res


        