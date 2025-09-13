class Solution:
    def maxDifference(self, s: str) -> int:

        res = []
        even = []
        odd = []

        for i in set(s):
            res.append(s.count(i))
    
        for i in res:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)

        if even == [] or odd == []:
            return 0

        return max(odd) - min(even)
        