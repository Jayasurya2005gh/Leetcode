class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dic = {}

        for i in strs:
            sort = sorted(i)
            sortj = "".join(sort)
            if sortj not in dic:
                dic[sortj] = [i]
            else:
                dic[sortj].append(i)
        return list(dic.values())
        