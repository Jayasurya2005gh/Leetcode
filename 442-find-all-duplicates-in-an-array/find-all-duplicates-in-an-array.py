class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        pre_res = set()
        res = []

        for i in nums:
            if i in pre_res:
                res.append(i)
            else:
                pre_res.add(i)
        return res