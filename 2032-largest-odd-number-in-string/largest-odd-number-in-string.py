class Solution:
    def largestOddNumber(self, num: str) -> str:

        nums = []

        for i in num:
            nums.append(int(i))

        curr_val = ""    
        for i in range(len(nums)):
            if nums[len(nums) - 1] % 2 != 0:
                for i in nums:
                    curr_val += str(i)
                return curr_val
            else:
                nums.pop(-1)
        return curr_val

        