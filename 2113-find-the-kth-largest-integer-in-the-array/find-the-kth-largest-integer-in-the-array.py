class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:

        res = []
        ans = 0

        for i in nums:
            res.append(int(i))
    
        res = sorted(res)
        res = res[::-1]

        for i in range(k):
            if i == k - 1:
                ans = res[i]
        
        return str(ans)
        