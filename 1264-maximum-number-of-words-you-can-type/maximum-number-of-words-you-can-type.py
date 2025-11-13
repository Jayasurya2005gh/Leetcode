class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:

        count = 0
        text = text.split()

        for i in text:
            if set(i) & set(brokenLetters):
                continue
            else:
                count += 1

        return count
        