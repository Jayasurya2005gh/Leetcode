class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:


        res = []
        intervals = sorted(intervals)

        for i in intervals:
            if res == [] or res[-1][1] < i[0]:
                res.append(i)
            else:
                res[-1][1] = max(res[-1][1],i[1])
        return res
            
        