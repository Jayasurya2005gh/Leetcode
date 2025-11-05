class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:

        dic = {}

        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        stock_num = dic[s[0]]
        for key,values in dic.items():
            if values == stock_num:
                continue
            else:
                return False
        return True
        