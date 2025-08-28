class Solution:
    def minLength(self, s: str) -> int:

        res = []
        for i in s:
            if res != [] and ((res[-1] == 'A' and i == 'B') or (res[-1] == 'C' and i == 'D')):
                res.pop()
            else:
                res.append(i)
        return len(res)


        