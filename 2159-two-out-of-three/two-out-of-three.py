class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:

        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        nums3 = sorted(set(nums3))

        dic = {}
        res = []

        for i in nums1:
            dic[i] = 1
    
        for i in nums2:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        
        for i in nums3:
            if i in dic:
                dic[i] += 1
        
        for key,value in dic.items():
            if value >= 2:
                res.append(key)
        
        return res
        