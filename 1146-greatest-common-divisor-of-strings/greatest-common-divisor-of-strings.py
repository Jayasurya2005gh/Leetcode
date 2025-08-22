import math
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:

        s1 = str1
        s2 = str2

        if s1 + s2 != s2 + s1:
            return ""

        a = math.gcd(len(s1),len(s2))
        return s1[:a]
        