class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:

        ans = []
        res = []

        for i in mat:
            ans.append(sum(i))

        values = sorted(ans)

        for i in range(k):
            curr_ind = ans.index(values[i])
            res.append(curr_ind)
            ans[curr_ind] = 101
        
        return res
        