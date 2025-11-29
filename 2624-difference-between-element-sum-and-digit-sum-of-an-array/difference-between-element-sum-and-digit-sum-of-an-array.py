class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:

        digit_sum = sum(nums)
        element_sum = 0

        for i in nums:
            i = str(i)
            for j in i:
                element_sum += int(j)

        res = digit_sum - element_sum
        return res

        
        