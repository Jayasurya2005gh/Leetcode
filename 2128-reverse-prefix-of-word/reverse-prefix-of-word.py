class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:

        if ch not in word:
            return word
            
        ind = word.index(ch)+1

        res = word[:ind]
        ans = word[ind:]

        res = res[::-1]
        return res + ans
        