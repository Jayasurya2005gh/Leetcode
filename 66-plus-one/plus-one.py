class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        res = ""
        ans = []
        
        for i in digits:
            res += str(i)
        res = str(int(res) + 1)

        for i in res:
            ans.append(int(i))
        return ans


        