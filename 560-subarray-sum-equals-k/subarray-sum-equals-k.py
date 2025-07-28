class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dic = {0:1}
        count = 0
        sums = 0

        for i in nums:
            sums += i
            if sums - k in dic:
                count += dic[sums-k]
            dic[sums] = dic.get(sums,0)+1
        return count

