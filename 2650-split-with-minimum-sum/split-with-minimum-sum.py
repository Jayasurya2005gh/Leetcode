class Solution:
    def splitNum(self, num: int) -> int:

        num1 = ""
        num2 = ""

        num = sorted(str(num))

        for i in range(len(num)):
            if i % 2 == 0:
                num1 += num[i]
            else:
                num2 += num[i]

        res = int(num1) + int(num2)
        return res
        