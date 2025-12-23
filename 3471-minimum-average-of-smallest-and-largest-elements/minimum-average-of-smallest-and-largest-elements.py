class Solution:
    def minimumAverage(self, nums: List[int]) -> float:

        max_num = 0
        min_num = 0
        res = []

        while nums != []:
            max_num = max(nums)
            min_num = min(nums)
            res.append((max_num + min_num) / 2)
            nums.remove(max_num)
            nums.remove(min_num)
    
        return min(res)
        