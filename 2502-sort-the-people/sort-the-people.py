class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:

        dic = {}
        res = []

        for i in range(len(names)):
            dic[heights[i]] = names[i]

        sorted_dic = dict(sorted(dic.items(), reverse = True))
        for value in sorted_dic.values():
            res.append(value)
        return res