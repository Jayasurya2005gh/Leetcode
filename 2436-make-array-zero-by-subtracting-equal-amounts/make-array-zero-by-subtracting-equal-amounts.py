class Solution:
    def minimumOperations(self, nums: List[int]) -> int:

        nums = sorted(nums)

        count = 0
        sub = 0

        while sum(nums) != 0:
            count += 1
            for i in nums:
                if i != 0:
                    sub = i
                    break

            for i in range(len(nums)):
                if nums[i] != 0:
                    nums[i] = nums[i] - sub
            

        return count