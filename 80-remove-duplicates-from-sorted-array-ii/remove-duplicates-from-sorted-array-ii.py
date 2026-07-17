class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        count = 0
        curr = nums[0]
        i = 0
        
        while i < len(nums):
            if curr == nums[i]:
                count += 1
                if count > 2:
                    nums.pop(i)
                else:
                    i += 1
            else:
                curr = nums[i]             
                count = 1
                i += 1













        







        