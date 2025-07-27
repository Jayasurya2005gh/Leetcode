class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        minise = -1
        for i,n in enumerate(nums):
            if n == target:
                return i
        return minise