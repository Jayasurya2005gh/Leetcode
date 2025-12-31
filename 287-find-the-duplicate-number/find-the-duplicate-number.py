class Solution:
    def findDuplicate(self, nums: List[int]) -> int:

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key,values in dic.items():
            if values >= 2:
                return key
                

        