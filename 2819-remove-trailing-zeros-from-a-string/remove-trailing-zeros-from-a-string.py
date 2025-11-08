class Solution:
    def removeTrailingZeros(self, num: str) -> str:

        if int(num[len(num) - 1]) != 0:
            return num
        else:
            count = 0
            for i in range(len(num) - 1, -1, -1):                
                if int(num[i]) != 0:
                    res = num[0:-count]
                    return res
                    break
                count += 1
        