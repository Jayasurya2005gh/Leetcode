class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:

        ans = 0

        for i in str(x):
            ans += int(i)

        if x % ans == 0:
            return ans
        return -1
        