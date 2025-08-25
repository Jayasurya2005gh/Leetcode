class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        nums = sorted(intervals)
        res = [nums[0]]

        for i in range(1,len(nums)):
            if res[-1][1] < nums[i][0]:
                res.append(nums[i])
            else:
                res[-1][1] = max(res[-1][1], nums[i][1])
        return res
        