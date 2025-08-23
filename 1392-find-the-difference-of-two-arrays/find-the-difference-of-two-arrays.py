class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:

        n1 = nums1
        n2 = nums2

        n1_res = []
        n2_res = []
        res = []
        for i in n1:
            if i not in n2 and i not in n1_res:
                n1_res.append(i)
        for i in n2:
            if i not in n1 and i not in n2_res:
                n2_res.append(i)

        res.append(n1_res)
        res.append(n2_res)
        return res
    
        