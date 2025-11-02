class Solution:
    def isValid(self, word: str) -> bool:

        nums = []
        vowels = []
        consonants = []

        if len(word) >= 3:
            for i in word:
                if i.isalpha():
                    if i in "aeiouAEIOU":
                        vowels.append(i)
                    else:
                        consonants.append(i)
                elif i.isdigit():
                    nums.append(i)
                else:
                    return False
        else:
            return False

        if vowels !=[] and consonants != []:
            return True
        return False
        