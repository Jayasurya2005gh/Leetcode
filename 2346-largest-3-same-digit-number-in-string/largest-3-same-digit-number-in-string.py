class Solution:
    def largestGoodInteger(self, num: str) -> str:

        res = []
        ans = "000"
        digits = 0

        for i in range(10):
            if str(ans) in num:
                res.append(str(ans))
            digits += 111
            ans = digits

        if res != []:
            return str(max(res))
        return ""
    
        