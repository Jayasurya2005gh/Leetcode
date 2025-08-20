class Solution:
    def firstUniqChar(self, s: str) -> int:

        dic = {}
        for i in s:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for i,n in enumerate(s):
            if dic[n] == 1:
                return i
        return -1