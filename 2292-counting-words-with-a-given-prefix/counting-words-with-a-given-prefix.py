class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:

        count = 0

        for i in words:
            if len(i) >= len(pref):
                words_pref = i[:len(pref)]
                if pref == words_pref:
                    count += 1            
        return count
        