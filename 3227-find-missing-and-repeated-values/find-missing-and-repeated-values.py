class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        res = []
        ans = []

        for i in grid:
            for j in i:
                res.append(j)

        res = sorted(res)
        res_set = list(set(res))

        for i in res_set:
            if res.count(i) > 1:
                ans.append(i)
                break

        for i in range(1,len(res) + 1):
            if i in res:
                continue
            else:
                ans.append(i)

        return ans
        
        