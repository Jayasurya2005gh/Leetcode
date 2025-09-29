class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:

        vowels = "aeiou"
        count = 0

        for i in range(left,right + 1):
            if len(words[i]) >= 2:
                if words[i][0] in vowels and words[i][len(words[i]) - 1] in vowels:
                    count += 1
            else:
                if words[i] in vowels:
                    count += 1            
        return count
        