class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        dic = {}
        count = 0

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        for key,values in dic.items():
            if values % k == 0:
                count += key * values

        return count
        