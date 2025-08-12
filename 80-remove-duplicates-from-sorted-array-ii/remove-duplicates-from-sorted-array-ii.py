class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        c = 1
        l = 1

        for r in range(1,len(nums)):
            if nums[r] == nums[r-1]:
                c += 1
            else:
                c = 1

            if c <= 2:
                nums[l] = nums[r]
                l += 1
        return l
        