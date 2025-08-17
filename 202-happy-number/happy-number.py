class Solution:
    def isHappy(self, n: int) -> bool:

        ans = str(n)
        seen = set()
        res = 0
        while ans != "1" and ans not in seen:
            seen.add(ans)          
            for i in ans:
                res += int(i) * int(i)
                ans = str(res)
            res = 0

        if ans == "1":
            return True
        else:
            return False
        