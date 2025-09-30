class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        nums = list(set(nums))
        ans = []
        res = []
    
        for i in nums:
            i = str(i)
            i = i[::-1]
            ans.append(abs(int(i)))
    
        final_res = nums + ans
        final_res = list(set(final_res))

        return len(final_res)
        