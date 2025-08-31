class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        s_join = "".join(s)
        rev_s = list(s_join[::-1])

        for i in range(len(s)):
            s[i] = rev_s[i]
        return s
    