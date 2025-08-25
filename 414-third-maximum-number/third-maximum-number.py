class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = []
        nums = set(nums)
        for i in nums:
            res.append(i)

        if len(res) >= 3:
            for i in range(2):
                res.remove(max(res))
            return max(res)
        
        elif len(res) == 2:
            nums = sorted(nums)
            a = res.pop(len(nums)-1)
            return a
        
        else:
            return max(res)
        