class Solution:
    def maximum69Number (self, num: int) -> int:

        res = [int(num)]
        ans = list(str(num))

        for i in range(len(ans)):
            if ans[i] == "9":
                ans[i] = "6"
            else:
                ans[i] = "9"

            res.append(int("".join(ans)))
            ans = list(str(num))

        return max(res)

        