class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:

        ans = s
        res = []

        while len(ans) % k != 0:
            ans += fill
    
        for i in range(0,len(ans),k):
            res.append(ans[i:i + k])
        
        return res
        