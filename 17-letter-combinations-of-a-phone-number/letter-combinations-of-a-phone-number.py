class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        
        dic = {2:'abc',3:'def',4:'ghi',5:'jkl',6:'mno',7:'pqrs',8:'tuv',9:'wxyz'}
        ans = []
        digit = digits

        if digit == "":
            return []

        for i in digit:
            ans.append(int(i))
    
        res = []
        for i in ans:
            res.append(dic[i])
    
        final = []
        
        if len(res) == 1:
            for i in res[0]:
                final.append(i)
            return final

        elif len(res) == 2:
            for i in res[0]:
                for j in res[1]:
                    final.append(i+j)
            return final

        elif len(res) == 3:
            for i in res[0]:
                for j in res[1]:
                    for k in res[2]:                        
                        final.append(i+j+k)
            return final

        elif len(res) == 4:
            for i in res[0]:
                for j in res[1]:
                    for k in res[2]:
                        for l in res[3]:                        
                            final.append(i+j+k+l)
            return final
        