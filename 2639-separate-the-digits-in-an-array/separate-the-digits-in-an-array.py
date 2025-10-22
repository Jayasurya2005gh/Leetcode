class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:

        res = []

        for i in nums:
            i = str(i)
            for j in i:
                res.append(int(j))

        return res
        