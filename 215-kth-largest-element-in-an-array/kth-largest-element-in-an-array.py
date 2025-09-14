class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:

        n = sorted(nums)
        n = n[::-1]
        res = n[k-1]
        return res
        