class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:


        res = nums
        res.append(target)
        res = sorted(res)
        for i,n in enumerate(nums):
            if n == target:
                return i
            return res.index(target)
            
        