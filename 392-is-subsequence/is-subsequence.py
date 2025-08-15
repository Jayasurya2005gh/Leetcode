class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        l = 0

        for r in range(len(t)):
            if l < len(s) and s[l] == t[r]:
                l += 1

        if len(s) == l:
            return True
        else:
            return False
        