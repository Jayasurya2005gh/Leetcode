class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # Take only the first m elements from nums1 (ignore placeholders)
        ans = nums1[:m]

        # Merge with nums2
        res = ans + nums2

        # Sort the merged list
        res.sort()

        # Update nums1 in-place
        for i in range(len(nums1)):
            nums1[i] = res[i]
