class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0
        allowed = set(allowed)

        for i in words:
            i = "".join(sorted(set(i)))
            curr_len = 0
            for j in i:
                if j in allowed:
                    curr_len += 1
                if curr_len == len(i):
                    count += 1
        return count
