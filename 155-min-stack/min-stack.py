class MinStack:

    def __init__(self):
        self.st1 = []
        self.st2 = []
        

    def push(self, val: int) -> None:
        self.st1.append(val)
        curr_min = self.st1[-1]
        for i in self.st1:
            if i < curr_min:
                curr_min = i
        self.st2.append(curr_min) 

        

    def pop(self) -> None:
        self.st1.pop()
        self.st2.pop()
        

    def top(self) -> int:
        return self.st1[-1]
        

    def getMin(self) -> int:
        return self.st2[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()