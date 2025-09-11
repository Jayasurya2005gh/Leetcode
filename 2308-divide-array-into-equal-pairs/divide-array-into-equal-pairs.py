class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        set_nums = list(set(nums))

        res = []
        count = 0

        for i in set_nums:
            res.append(nums.count(i))

        for i in res:
            if i % 2 == 0:
                continue
            else:
                count += 1 

        if count == 0:
            return True
        else:
            return False

        