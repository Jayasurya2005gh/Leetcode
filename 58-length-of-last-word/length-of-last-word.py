class Solution:
    def lengthOfLastWord(self, s: str) -> str:

        res = ""
        s = s.strip()
        s_split = s.split()
        rev = s_split[::-1]

        res = rev[0]
        return len(res)

        