class Solution:
    def addDigits(self, num: int) -> int:

        res = str(num)
        curr_num = 0

        while len(res) != 1:
            for i in res:
                curr_num += int(i)
            res = str(curr_num)
            curr_num = 0

        return int(res)
        