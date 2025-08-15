class Solution:
    def reverseWords(self, s: str) -> str:

        s = s.strip()
        s_split = s.split()
        rev = s_split[::-1]
        rev_join = " ".join(rev)
        return rev_join
        