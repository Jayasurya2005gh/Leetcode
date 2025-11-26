class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:

        count = 0
        allowed = "".join(sorted(set(allowed)))

        for i in words:
            i = "".join(sorted(set(i)))
            if len(i) < len(allowed):
                if set(i).issubset(set(allowed)):
                    count += 1
            else:
                if i in allowed:
                    count += 1
        return count
