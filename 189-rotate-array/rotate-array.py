class Solution:
    def rotate(self, nums: List[int], k: int) -> None:

        k = k % len(nums)
        ans1 = nums[-k:]
        ans2 = nums[:-k]

        result = ans1 + ans2
        for i in range(len(nums)):
            nums[i] = result[i]
        return result