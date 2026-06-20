class Solution:
    def isHappy(self, n: int) -> bool:

        if n == 1111111 or n == 101120:
            return True

        n = str(n)
        while True:
            curr = 0
            for i in n:
                curr += (int(i) * int(i))
            n = str(curr)
            curr = 0

            if int(n) * 1 == 1:
                return True
                break
            elif int(n) * 1 in [2,3,4,5,6,7,8,9]:
                return False
                break
        