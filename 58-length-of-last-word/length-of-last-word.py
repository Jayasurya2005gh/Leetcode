class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        s = list(s.strip().split())
        res = s[-1]
        return len(res)
        