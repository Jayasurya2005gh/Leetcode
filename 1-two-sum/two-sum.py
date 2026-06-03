class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        left = 0
        right = 1

        res = []

        while left != len(nums):
            for right in range(left + 1,len(nums)):
                if nums[left] + nums[right] == target:
                    res.append(left)
                    res.append(right)
            left += 1

        return res



        
        