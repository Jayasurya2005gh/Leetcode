class Solution:
    def frequencySort(self, s: str) -> str:

        dic = {}
        res = ""

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        while dic != {}:
            max_key = max(dic, key = dic.get)
            count = dic[max_key]
            res += max_key * count
            del(dic[max_key])

        return res
        