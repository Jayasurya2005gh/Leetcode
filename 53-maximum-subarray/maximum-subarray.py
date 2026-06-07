class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        total = nums[0]
        curr = 0

        for i in nums:
            if curr < 0:
                curr = 0
            curr += i

            if curr > total:
                total = curr

        return total