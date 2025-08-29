class Solution:
    def minLength(self, s: str) -> int:

        res = []

        for i in s:
            if res != []:
                if res[-1] == 'A' and i  == 'B':
                    res.pop()
                elif res[-1] == 'C' and i == 'D':
                    res.pop()
                else:
                    res.append(i)
            else:
                res.append(i)

        return len(res)
        