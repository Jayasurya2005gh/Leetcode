class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        res = []
        spec = ("+","-","*","/")
        for i in tokens:
            if i not in spec:
                res.append(int(i))
            else:
                a = res.pop()
                b = res.pop()
                if i == "+":
                    res.append(a+b)
                elif i == "*":
                    res.append(a*b)
                elif i == "-":
                    res.append(b-a)
                elif i == "/":
                    res.append(int(b/a))
        ans = res.pop()
        return ans
        