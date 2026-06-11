class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}

        for i in nums:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        sorted_dic = dict(sorted(dic.items(), key = lambda x : x[1], reverse = True))
        res = []
        ans = 0

        for key in sorted_dic.keys():
            if ans == k:
                break
            else:
                res.append(key)
                ans += 1
        return res