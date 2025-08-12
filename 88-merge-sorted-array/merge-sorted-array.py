class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        res = []

        for i in range(m):
            res.append(nums1[i])
        
        ans = res + nums2
        sort = sorted(ans)
        
        for i in range(len(nums1)):
            nums1[i] = sort[i]
        return sort
        