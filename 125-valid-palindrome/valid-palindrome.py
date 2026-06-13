class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ""

        for i in s:
            if i.isalnum():
                res += i.lower()
        rev_res = res[::-1]
        if res == rev_res:
            return True
        return False
        