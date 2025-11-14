class Solution:
    def minimizedStringLength(self, s: str) -> int:

        res = []

        for i in s:
            if i not in res:
                res.append(i)

        ans = len(res)
        return ans
        