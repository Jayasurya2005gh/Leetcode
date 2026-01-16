class Solution:
    def largestEven(self, s: str) -> str:

        nums = list(s)
        last_val = len(nums) - 1

        while len(nums) != 1:
            if int(nums[last_val]) % 2 == 0:
                return "".join(nums)
            else:
                nums.pop(last_val)
                last_val -= 1

        if int(nums[-1]) % 2 == 0:
            return nums[-1]
        return ""
        