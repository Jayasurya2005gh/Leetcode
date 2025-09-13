class Solution:
    def maxFreqSum(self, s: str) -> int:

        res = []
        ans = []
        dicvow = {}
        diccon = {}
        max_dicvow = 0
        max_diccon = 0

        for i in s:
            if i in "aeiouAEIOU":
                res.append(i)
            else:
                ans.append(i)

        for i in set(res):
            dicvow[i] = res.count(i)

        for i in set(ans):
            diccon[i] = ans.count(i)

        if dicvow != {}:
            max_dicvow = max(dicvow.values())
        else:
            max_dicvow = 0

        if diccon != {}:
            max_diccon = max(diccon.values())
        else:
            max_diccon = 0

        final_res = max_dicvow + max_diccon
        return final_res

        
        