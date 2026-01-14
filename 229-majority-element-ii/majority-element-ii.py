class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        res = []
        limit = len(nums) // 3

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key,values in dic.items():
            if values > limit:
                res.append(key)

        return res
        