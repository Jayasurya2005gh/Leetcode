class Solution:
    def isPerfectSquare(self, num: int) -> bool:

        res = int(num ** 0.5)

        if res * res == num:
            return True
        else:
            return False
        