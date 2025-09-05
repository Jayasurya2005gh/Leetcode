class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        res = []
        for i in nums:
            if len(str(i)) % 2 == 0:
                res.append(str(i))

        count = 0
        for i in res:
            if len(i) % 2 == 0:
                count += 1
        
        return count
        