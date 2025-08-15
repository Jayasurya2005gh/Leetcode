class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran = ransomNote
        mag = list(magazine)
        count = 0

        for i in ran:
            if i in mag:
                mag.remove(i)
                count += 1

        if len(ran) == count:
            return True
        else:
            return False
            
            
        