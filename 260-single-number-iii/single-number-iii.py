class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:

        dic = {}
        res = []

        for i in nums:
            count = nums.count(i)
            dic[i] = count

        for i in nums:
            if dic[i] == 1:
                res.append(i)
        return res

        