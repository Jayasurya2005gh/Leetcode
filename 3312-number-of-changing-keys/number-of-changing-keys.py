class Solution:
    def countKeyChanges(self, s: str) -> int:

        res = s.lower()
        count = 0

        for i in range(1,len(res)):
            if res[i] != res[i - 1]:
                count += 1

        return count
        