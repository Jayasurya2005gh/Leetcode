class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        hash = {}
        for i in strs:
            sort = "".join(sorted(i))
            if sort not in hash:
                hash[sort] = [i]
            else:
                hash[sort].append(i)
        return list(hash.values())
        