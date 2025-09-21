class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        res = []
        ans = []

        for i in range(len(names)):
            res.append([names[i], heights[i]])

        sorted_res = sorted(res, key = lambda x : x[1])

        for i in sorted_res:
            ans.append(i[0])

        ans = ans[::-1]
        return ans
        