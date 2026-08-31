class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        length = len(temperatures)
        stk = []
        res = [0] * length
        for i in range(length):
            if i == 0:
                stk.append((temperatures[i], i))
            else:
                while stk and stk[-1][0] < temperatures[i]:
                    temp = stk.pop()
                    res[temp[1]] = i - temp[1]
                stk.append((temperatures[i], i))
        return res


