class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        res = []

        for i in nums1:
            res.append(i)
        for i in nums2:
            res.append(i)
        
        res = sorted(res)
        if len(res) % 2 != 0:
            median = len(res) // 2
            return res[median]
        else:
            median = (res[len(res) // 2] + res[len(res) // 2 - 1]) / 2
            return median
        