class MinStack:

    def __init__(self):
        self.stack = []
        self.minim = float('inf')
        
    def push(self, val: int) -> None:
        self.stack.append((val,min(self.minim,val)))
        self.minim = min(self.minim,val)

    def pop(self) -> None:
        self.stack.pop()
        if self.stack:
            self.minim = self.stack[-1][1]
        else:
            self.minim = float('inf')

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None
        
    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None

        
