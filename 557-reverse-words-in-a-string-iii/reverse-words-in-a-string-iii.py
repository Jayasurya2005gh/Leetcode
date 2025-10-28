class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.split()
        res = []

        for i in s:
            curr_i = ""
            rev_i = i[::-1]
            curr_i = rev_i
            res.append(curr_i)

        ans = " ".join(res)
        return ans

        