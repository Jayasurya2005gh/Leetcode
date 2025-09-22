class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:

        nums_set = sorted(set(nums))
        res = []

        for i in nums_set:
            res.append(nums.count(i))
    
        max_count = max(res)

        total = 0
        for i in res:
            if i == max_count:
                total += i 

        return total
        