class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:

        dic = {"++X" : 1, "X++" : 1, "--X" : -1, "X--" : -1}
        res = 0

        for i in operations:
            res += dic[i]

        return res

        