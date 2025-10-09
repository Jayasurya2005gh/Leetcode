class Solution:
    def distinctAverages(self, nums: List[int]) -> int:

        res = set()

        while nums != []:
            a = max(nums)
            b = min(nums)
    
            res.add((a + b) / 2)
    
            nums.remove(a)
            nums.remove(b)
    
        return len(res)
        