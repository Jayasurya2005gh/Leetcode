class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        ans = set()
        res = []

        for i in nums:
            if i in ans:
                res.append(i)
            else:
                ans.add(i)
        return res
        