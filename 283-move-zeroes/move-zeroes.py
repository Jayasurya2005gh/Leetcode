class Solution:
    def moveZeroes(self, nums: List[int]) -> None:

        ans1 = []
        ans2 = []
        res = []

        for i in nums:
            if i == 0:
                ans2.append(i)
            else:
                ans1.append(i)

        res = ans1 + ans2
        for i in range(len(nums)):
            nums[i] = res[i]
        return res