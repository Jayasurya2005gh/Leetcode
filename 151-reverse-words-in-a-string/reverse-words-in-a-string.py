class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip().split()
        res = s[::-1]

        return " ".join(res)
        