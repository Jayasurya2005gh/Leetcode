class Solution:
    def findLucky(self, arr: List[int]) -> int:

        dic = {}

        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1
        
        max_key = -1
        for key,value in dic.items():
            if key == value:
                max_key = max(max_key,key)
        return max_key
        