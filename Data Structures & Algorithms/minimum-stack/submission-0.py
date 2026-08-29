class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []

    def push(self, val: int) -> None:
        if not self.stk: 
            self.minstk.append(val)
            self.stk.append(val)
        else:
            self.minstk.append(min(self.minstk[-1], val))
            self.stk.append(val)

    def pop(self) -> None:
        self.stk.pop()
        self.minstk.pop()

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        if self.minstk:
            return self.minstk[-1]
        else:
            return None
