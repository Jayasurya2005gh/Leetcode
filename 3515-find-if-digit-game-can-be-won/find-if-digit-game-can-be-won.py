class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        a = 0
        b = 0
        for i in nums:
            if len(str(i)) == 1:
                a += i
            else:
                b += i
        return True if a != b else False