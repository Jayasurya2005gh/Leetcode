class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:

        curr_org = original
        for i in range(len(nums)):
            if curr_org in nums:
                curr_org = curr_org * 2            
        return curr_org
        