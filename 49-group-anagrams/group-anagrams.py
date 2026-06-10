class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dic = {}
        res = []

        for i in strs:
            sort_i = sorted(list(i))
            rev_i = "".join(sort_i)
            if rev_i not in dic:
                dic[rev_i] = [strs.index(i)]
            else:
                dic[rev_i].append(strs.index(i))
        
        for i in dic.values():
            curr_res = []
            for j in i:
                curr_res.append(strs[j])
            res.append(curr_res)
        
        return res
        