class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0:1}
        count = 0
        s = 0
        
        for i in nums:
            s += i
            if s-k in dic:
                count += dic[s-k]
            dic[s] = dic.get(s,0)+1
        return count