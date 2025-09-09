class Solution:
    def sortSentence(self, s: str) -> str:
        
        s = s.split()
        s = sorted(s)
        res = []

        for i in range(1,len(s)+1):
            for word in s:
                if word[-1] == str(i):
                    res.append(word[0:len(word)-1])    
        return " ".join(res)    
    
        