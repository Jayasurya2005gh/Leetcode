class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        res = []
        ans = []
        count = 0

        for i in nums:
            if i == 0:
                count += 1
            else:
                res.append(i)

        ans = res + [0] * count
        for i in range(len(nums)):
            nums[i] = ans[i]
        return ans                