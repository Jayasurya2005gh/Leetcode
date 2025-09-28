class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:

        n = sorted(str(n))
        dic = {}

        for i in n:
            if int(i) not in dic:
                dic[int(i)] = 1
            else:
                dic[int(i)] += 1

        count = 100000000
        least_key = 0

        for key,value in dic.items():
            if value < count:
                count = value
                least_key = key

        return least_key
    
    
        