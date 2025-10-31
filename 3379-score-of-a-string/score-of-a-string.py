class Solution:
    def scoreOfString(self, s: str) -> int:

        curr_ord_val = ord(s[0])
        res = []

        for i in range(1,len(s)):
            res.append(abs(curr_ord_val - ord(s[i])))
            curr_ord_val = ord(s[i])
    
        ans = sum(res)
        return ans
    
        