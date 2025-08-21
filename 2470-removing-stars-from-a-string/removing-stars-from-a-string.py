class Solution:
    def removeStars(self, s: str) -> str:

        ans = []
        for i in s:
            if i != "*":
                ans.append(i)
            else:
                ans.pop()

        res = ""
        while ans:
            res += ans.pop(0)

        return res
        