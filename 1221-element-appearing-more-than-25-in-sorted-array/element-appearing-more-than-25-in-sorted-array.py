class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:

        dic = {}

        for i in arr:
            if i not in dic:
                dic[i] = 1
            else:
                dic[i] += 1

        max_key = 0
        max_value = 0

        for key,value in dic.items():
            if value > max_value:
                max_value = value 
                max_key = key 

        if len(arr) == 1:
            return arr[0]

        elif max_value >= 2:
            return max_key
        