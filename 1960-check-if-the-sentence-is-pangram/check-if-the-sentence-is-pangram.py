class Solution:
    def checkIfPangram(self, sentence: str) -> bool:

        alphabets = "abcdefghijklmnopqrstuvwxyz"
        res = sorted(set(sentence))

        ans = "".join(res)
        if ans == alphabets:
            return True
        return False
        
        