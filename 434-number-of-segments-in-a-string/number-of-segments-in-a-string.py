class Solution:
    def countSegments(self, s: str) -> int:

        s = s.split()
        res = []

        for i in s:
            res.append(i)

        return len(res)
        