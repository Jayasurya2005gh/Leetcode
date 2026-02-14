class Solution:
    def generateTheString(self, n: int) -> str:

        res = ""
        if n % 2 == 0:
            for i in range(n):
                if i == n - 1:
                    res += "b"
                else:
                    res += "a"
        else:
            for i in range(n):
                res += "a"

        return res
        