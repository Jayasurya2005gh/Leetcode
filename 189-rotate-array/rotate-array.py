class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)
        ans = nums[:-k]
        res = nums[-k:]

        result = res + ans
        for i in range(len(nums)):
            nums[i] = result[i]