class Solution:
    def areNumbersAscending(self, s: str) -> bool:

        s = s.split()
        res = []

        for i in s:
            if i.isdigit():
                res.append(int(i))
        
        ans = sorted(set(res))

        if ans == res:
            return True
        else:
            return False
        