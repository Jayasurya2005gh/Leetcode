class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:

        intervals.append(newInterval)
        nums = sorted(intervals)
        res = [nums[0]]

        for i in range(1,len(nums)):
            if res[-1][1] < nums[i][0]:
                res.append(nums[i])
            else:
                res[-1][1] = max(res[-1][1],nums[i][1])
        return res
        