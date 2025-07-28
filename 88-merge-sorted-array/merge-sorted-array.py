class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        ans = nums1[:m]
        res = ans + nums2
        sort = sorted(res)

        for i in range(len(nums1)):
            nums1[i] = sort[i]
