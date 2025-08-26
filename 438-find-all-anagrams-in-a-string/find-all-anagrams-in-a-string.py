class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        k = len(p)
        p = "".join(sorted(p))
        res = []
        ans = []

        for i in range(len(s) - k + 1):
            res.append(s[i:i+k])

        for i in range(len(res)):
            a = res.pop(0)
            a = "".join(sorted(a))
            if p == a:
                ans.append(i)

        return ans
        