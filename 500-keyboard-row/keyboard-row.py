class Solution:
    def findWords(self, words: List[str]) -> List[str]:

        dic = {1:"eiopqrtuwy",2:"adfghjkls",3:"bcmnvxz"}
        res = []
        ans = []

        for i in words:
            res.append(i.lower())
        
        for i in range(len(res)):
            if set(res[i]).issubset(set(dic[1])):
                ans.append(words[i])

            elif set(res[i]).issubset(set(dic[2])):
                ans.append(words[i])

            elif set(res[i]).issubset(set(dic[3])):
                ans.append(words[i])

        return ans
        