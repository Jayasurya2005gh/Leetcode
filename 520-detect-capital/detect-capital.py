class Solution:
    def detectCapitalUse(self, word: str) -> bool:

        n = word

        if word == n.upper():
            return True
        elif word == n.lower():
            return True
        elif word == n.capitalize():
            return True
        else:
            return False
        