class Solution:
    def firstPalindrome(self, words: List[str]) -> str:

        res = ""

        for i in words:
            rev_i = i[::-1]
            if i == rev_i:
                res = i
                break

        return res
        