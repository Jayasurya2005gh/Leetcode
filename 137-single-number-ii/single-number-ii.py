class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = sorted(set(nums))

        for i in ans:
            if nums.count(i) == 1:
                return i

        

        