class MinStack:

    def __init__(self):
        self.stack = []
        self.miniVal = float('inf')

    def push(self, val: int) -> None:
        curr_min = val if not self.stack else min(val, self.getMin())
        self.stack.append((val, curr_min))

    def pop(self) -> None:
        return self.stack.pop()
        
        

    def top(self) -> int:
        return self.stack[-1][0]
        

    def getMin(self) -> int:
        return self.stack[-1][1]


        
