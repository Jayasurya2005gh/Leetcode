class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:

        nums = sorted(nums)
        res = []
        num = nums[0]

        while num != max(nums):
            if num + 1 not in nums:
                res.append(num + 1)
                num = num + 1
            else:
                num = num + 1

        return res

        