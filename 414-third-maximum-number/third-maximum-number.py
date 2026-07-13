class Solution:
    def thirdMax(self, nums: List[int]) -> int:

        res = []
        for i in nums:
            if i not in res:
                res.append(i)

        if len(res) >= 3:
            for i in range(2):
                res.remove(max(res))
            return max(res)
        
        elif len(res) < 3:
            return max(res)
        