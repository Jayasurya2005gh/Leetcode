class Solution:
    def countGoodSubstrings(self, s: str) -> int:

        k = 3
        res = []
        count = 0

        for i in range(len(s) - k + 1):
            res.append(s[i : i + k])

        for i in res:
            i = set(i)
            if len(i) == 3:
                count += 1
        
        return count
        