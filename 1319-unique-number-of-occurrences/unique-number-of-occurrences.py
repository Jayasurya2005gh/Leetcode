class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:

        res = []
        arr_set = set(arr)
        for i in arr_set:
            if arr.count(i) not in res:
                res.append(arr.count(i))
            else:
                return False
        return True
        