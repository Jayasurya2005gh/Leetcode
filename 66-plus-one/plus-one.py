class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        ans = ""
        res = []
        


        for i in digits:
            ans += str(i)
        ans = str(int(ans) + 1)

        for i in ans:
            res.append(int(i))

        return res
        

        

        