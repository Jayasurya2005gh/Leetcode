class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        nums = sorted(nums)

        left = 0
        for right in range(1,len(nums)):
            if nums[right] == nums[left]:
                return True
            else:
                left += 1
        return False
        