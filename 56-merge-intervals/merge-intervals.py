class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        nums = sorted(intervals)
        res = [nums[0]]

        for i in nums:
            if res[-1][1] < i[0]:
                res.append(i)
            else:
               res[-1][1] = max(res[-1][1],i[1])
        return res
        