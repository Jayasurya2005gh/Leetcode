class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        res = nums[0]
        count = 0

        for i in nums:
            if count < 0:
                count = 0
            count += i
            if count > res:
                res = count
        return res
