class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:

        res = []

        while nums != []:
    
            a = min(nums)
            nums.remove(a)
    
            b = min(nums)
            nums.remove(b)
    
            res.append(b)
            res.append(a)
    
        return res
        