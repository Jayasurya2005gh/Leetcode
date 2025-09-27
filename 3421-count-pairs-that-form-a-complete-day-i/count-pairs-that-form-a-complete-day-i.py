class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:

        res = []
        count = 0

        for i in range(0,len(hours)):
            for j in range(i+1,len(hours)):
                res.append([hours[i],hours[j]])
        
        for i in res:
            if i[0] + i[1] == 24:
                count += 1
            elif (i[0] + i[1]) % 24 == 0:
                count += 1        
        return count
        