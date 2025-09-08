class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:

        res = []
        max_arr = max(arr)

        for i in range(1,max_arr + 1):
            if i not in arr:
                res.append(i)

        for i in range(max_arr + 1,max_arr + k + 1):
            res.append(i)
        
        return res[k-1]


       



        