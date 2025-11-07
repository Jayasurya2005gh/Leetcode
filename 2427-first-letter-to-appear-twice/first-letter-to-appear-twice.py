class Solution:
    def repeatedCharacter(self, s: str) -> str:

        set_res = set()

        for i in s:
            if i in set_res:
                return i
            else:
                set_res.add(i)
        