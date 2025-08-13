class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)
        ans1 = nums[:-k]
        ans2 = nums[-k:]

        res = ans2 + ans1
        for i in range(len(nums)):
            nums[i] = res[i]
        return res
        