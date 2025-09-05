class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        res = []

        for i in arr:
            res.append(i)
            if i == 0:
                res.append(0)

        for i in range(len(arr)):
            arr[i] = res[i]

        return arr
        