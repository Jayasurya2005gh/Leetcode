class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        ran = ransomNote
        mag = magazine
        count = 0
        mag_list = list(mag)
        for i in ran:
            if i in mag_list:
                mag_list.remove(i)
                count += 1
        if count == len(ran):
            return True
        else:
            return False

        