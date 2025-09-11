class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:

        res = []

        for i in nums:
            if nums.count(i) == 1:
                res.append(i)
        
        ans = sum(res)
        return ans
        