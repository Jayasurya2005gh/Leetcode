class Solution:
    def halvesAreAlike(self, s: str) -> bool:

        mid = len(s) // 2
        half1 = s[:mid]
        half2 = s[mid:]

        vowels = "aeiouAEIOU"
        count1 = 0
        count2 = 0


        for i in half1:
            if i in vowels:
                count1 += 1
        
        for i in half2:
            if i in vowels:
                count2 += 1
        
        if count1 == count2:
            return True
        else:
            return False
        