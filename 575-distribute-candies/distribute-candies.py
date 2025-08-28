class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:

        can = candyType

        rem_dup = len(set(can))
        can_div = len(can)//2
        return min(rem_dup,can_div)
        