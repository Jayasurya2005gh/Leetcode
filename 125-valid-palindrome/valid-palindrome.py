class Solution:
    def isPalindrome(self, s: str) -> bool:

        res = ""
        for i in s:
            if i.isalnum():
                res += i.lower()
        
        rev_res = res[::-1]
        if rev_res == res:
            return True
        else:
            return False
        