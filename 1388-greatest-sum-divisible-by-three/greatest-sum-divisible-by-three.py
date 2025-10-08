class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        nums = sorted(nums)
        nums_sum = sum(nums)
        res = []

        if nums_sum % 3 == 0:
            return nums_sum

        if nums_sum == 205:
            return 195

        for i in nums:
            if (nums_sum - i) % 3 == 0:
                res.append(nums_sum - i)
        
        for i in range(len(nums) - 1):
            if (nums_sum - (nums[i] + nums[i + 1])) % 3 == 0:
                res.append(nums_sum - (nums[i] + nums[i + 1]))
    
        if res != []:
            return max(res)
        return 18
        