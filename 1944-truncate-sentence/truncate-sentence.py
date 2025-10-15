class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        
        words = s.split()
        res = []

        for i in range(k):
            res.append(words[i])

        return " ".join(res)
        