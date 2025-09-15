class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:

        odd = []
        even = []
        res = []

        for i,n in enumerate(nums):
            if i % 2 == 0:
                even.append(n)
            else:
                odd.append(n)

        odd = sorted(odd)
        odd = odd[::-1]
        even = sorted(even)

        for i in range(len(nums)):
            if i % 2 == 0:
                res.append(even[i // 2])
            else:
                res.append(odd[i // 2])
        return res
        