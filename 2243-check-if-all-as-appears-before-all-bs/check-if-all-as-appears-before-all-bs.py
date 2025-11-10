class Solution:
    def checkString(self, s: str) -> bool:

        ans = sorted(s)
        res = "".join(ans)

        if res == s:
            return True
        return False
        