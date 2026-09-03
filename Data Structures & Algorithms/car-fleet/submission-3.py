class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        nArr = [(p, s) for p, s in zip(position, speed)]
        nArr.sort(reverse=True)
        stk = []
        for p, s in nArr:
            stk.append((target - p) / s)
            if len(stk) > 1 and stk[-2] >= stk[-1]:
                stk.pop()
        return len(stk)