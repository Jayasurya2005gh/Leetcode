class Solution:
    def canJump(self, nums: List[int]) -> bool:

        last_ind = len(nums)-1

        for i in range(len(nums)-2,-1,-1):
            if nums[i] + i >= last_ind:
                last_ind = i
        if last_ind == 0:
            return True
        else:
            return False


        