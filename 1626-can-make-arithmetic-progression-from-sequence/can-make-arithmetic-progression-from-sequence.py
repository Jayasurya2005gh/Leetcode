class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:

        arr = sorted(arr)
        l = 0
        r = 1
        prev_sum = arr[l] - arr[r]

        for r in range(1,len(arr)):
            if arr[l] - arr[r] == prev_sum:
                l += 1
            else:
                return False
        return True

        