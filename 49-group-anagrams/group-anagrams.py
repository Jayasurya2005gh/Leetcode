class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for i in strs:
            sort = "".join(sorted(i))
            if sort not in dic:
                dic[sort] = [i]
            else:
                dic[sort].append(i)
        return list(dic.values())