class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:

        sort_arr = sorted(set(arr))
        dic = {}
        res = []

        for i,n in enumerate(sort_arr):
            dic[n] = i + 1
    
        for i in arr:
            res.append(dic[i])
    
        return res
        