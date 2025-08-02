class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        
        res = 0
        ans = set(nums)

        for i in range(1,len(nums)+1):
            if i not in ans:
                res = i
        return res