class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:

        res = []
        final_res = []

        for word in words:
            ans = ""
            word = word.replace(separator," ")
            for i in word:
                if i == " ":
                    res.append(ans)
                    ans = ""
                else:
                    ans += i
            res.append(ans)

        for i in res:
            if i != '':
                final_res.append(i)        
        return final_res
        