class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:

        dic = {"a" : 0,"b" : 1,"c" : 2,"d" : 3,"e" : 4,"f" : 5,"g" : 6,"h" : 7,"i" : 8,"j" : 9,"k" : 10,"l" : 11,"m" : 12,"n" : 13,"o" : 14,"p" : 15,"q" : 16,"r" : 17,"s" : 18,"t" : 19,"u" : 20,"v" : 21,"w" : 22,"x" : 23,"y" : 24,"z" : 25}
        sum_firstWord = ""
        sum_secondWord = ""
        sum_targetWord = ""

        for i in firstWord:
            sum_firstWord += str(dic[i])
    
        for i in secondWord:
            sum_secondWord += str(dic[i])
    
        for i in targetWord:
            sum_targetWord += str(dic[i])
    
        res = int(sum_firstWord) + int(sum_secondWord)
        if int(sum_targetWord) == res:
            return True
        return False
        