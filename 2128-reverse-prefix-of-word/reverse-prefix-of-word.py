class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word:
            return word
        
        ind = word.index(ch)+1
        res1 = word[:ind]
        res2 = word[ind:]

        res1 = res1[::-1]
        return res1 + res2