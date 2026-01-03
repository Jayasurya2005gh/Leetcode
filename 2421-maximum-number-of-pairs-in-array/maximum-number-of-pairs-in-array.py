class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:

        nums = sorted(nums)
        ans = sorted(set(nums))
        count = 0
        
        for i in ans:
            while nums.count(i) >= 2:
                if nums.count(i) >= 2:
                    nums.remove(i)
                    nums.remove(i)
                    count += 1

        if nums != []:
            return [count,len(nums)]
        else:
            return [count,0]

        