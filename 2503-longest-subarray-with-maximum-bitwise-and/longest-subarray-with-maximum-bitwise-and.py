class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        max_num = max(nums)
        count = 0
        max_len = 0
        for i in nums:
            if i == max_num:
                count += 1
                max_len = max(max_len,count)
            else:
                count = 0
        return max_len

