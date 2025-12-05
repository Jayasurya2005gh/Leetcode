class Solution:
    def numberOfMatches(self, n: int) -> int:

        ans = n
        count = 1

        if ans < 2:
            return 0

        while ans != 2:
            if ans % 2 == 0:
                count += ans // 2
                ans = ans // 2
            else:
                count += (ans - 1) // 2
                ans = (ans - 1) // 2
                ans += 1

        return count
        