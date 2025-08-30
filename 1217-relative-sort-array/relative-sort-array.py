class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        res = []
        ans = []
        final = []

        for i in arr2:
            if i in arr1:
                count = arr1.count(i)
                res.append([i] * count)
        
        for i in arr1:
            if i not in arr2:
                ans.append(i)
        ans = sorted(ans)

        for i in res:
            for j in i:
                final.append(j)
        return final + ans



        