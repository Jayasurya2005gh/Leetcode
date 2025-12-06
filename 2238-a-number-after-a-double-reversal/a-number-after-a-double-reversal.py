class Solution:
    def isSameAfterReversals(self, num: int) -> bool:

        num = str(num)
        rev1 = num[::-1]
        rev1 = str(int(rev1))        
        rev2 = rev1[::-1]

        if rev2 == num:
            return True
        return False
        