class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:

        res = []
        can = candies
        excan = extraCandies

        for i in can:
            if i + excan >= max(can):
                res.append(True)
            else:
                res.append(False)
        return res

        
        