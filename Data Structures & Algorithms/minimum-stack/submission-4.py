class MinStack:

    def __init__(self):
        self.stk = []
        self.minimum = float('inf')

    def push(self, val: int) -> None:
        if not self.stk:
            self.stk.append(0)
            self.minimum = val
        else:
            self.stk.append(val - self.minimum)
            if val < self.minimum:
                self.minimum = val

    def pop(self) -> None:
        if not self.stk:
            return None
        p = self.stk.pop()
        if p < 0:
            self.minimum = self.minimum - p

    def top(self) -> int:
        t = self.stk[-1]
        if t < 0:
            return self.minimum
        else:
            return t + self.minimum

    def getMin(self) -> int:
        return self.minimum
        
