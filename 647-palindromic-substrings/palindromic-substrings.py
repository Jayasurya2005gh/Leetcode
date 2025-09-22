class Solution:
    def countSubstrings(self, s: str) -> int:

        res = []

        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                res.append(s[i:j])

        count = len(s)
        for i in res:
            rev_i = i[::-1]
            if len(i) >= 2 and rev_i == i:
                count += 1 
        
        return count
        