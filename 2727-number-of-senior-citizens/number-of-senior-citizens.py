class Solution:
    def countSeniors(self, details: List[str]) -> int:

        count = 0

        for i in details:
            curr_age = i[11:13]
            if int(curr_age) > 60:
                count += 1

        return count
        