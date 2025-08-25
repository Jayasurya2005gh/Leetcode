class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        if s == "":
            return t

        ans = []
        for i in t:
            ans.append(i)
        
        for i in s:
            if i in ans:
                ans.remove(i)
        return "".join(ans)
        