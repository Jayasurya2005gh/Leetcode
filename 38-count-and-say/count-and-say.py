class Solution:
    def countAndSay(self, n: int) -> str:
        
        n = n-1
        s = "1"
        for i in range(n):
            s = "".join(str(len(list(group))) + digit for digit, group in groupby(s))
        return s
