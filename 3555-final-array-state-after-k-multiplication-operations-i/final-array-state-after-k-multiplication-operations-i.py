class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:

        for i in range(k):
            curr_min = min(nums)
            curr_min_ind = nums.index(curr_min)
            nums[curr_min_ind] = (curr_min * multiplier)
        return nums
        