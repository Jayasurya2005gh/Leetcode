class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        res = []

        for i in nums:
            i = str(i)
            if not i.isdigit() and abs(int(i)) in nums:
                res.append(abs(int(i)))
        
        if res == []:
            return -1
        else:
            return max(res)
            
        