class Solution:
    def greatestLetter(self, s: str) -> str:

        res = sorted(s)
        res = res[::-1]
        ans = ""

        for i in res:
            if i == i.lower():
                if i.upper() in res:
                    ans = i.upper()
                    break
            elif i == i.upper():
                if i.lower() in res:
                    ans = i.upper()
                    break
        
        return ans

        