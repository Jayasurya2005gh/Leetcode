class Solution:
    def numberOfSpecialChars(self, word: str) -> int:

        word_lower = list(set())
        word_upper = list(set())
        count = 0

        for i in word:
            if i == i.lower() and i not in word_lower:
                word_lower.append(i)
            
            elif i == i.upper() and i not in word_upper:
                word_upper.append(i)

        for i in word_lower:
            if i.upper() in word_upper:
                count += 1
        
        return count
        