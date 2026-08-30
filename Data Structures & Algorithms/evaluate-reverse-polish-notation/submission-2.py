class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        oper = {'+', '-', '*', '/'}
        for token in tokens:
            if token in oper:
                if token == '+':
                    val = stk[-2] + stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(val)
                if token == '-':
                    val = stk[-2] - stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(val)
                if token == '*':
                    val = stk[-2] * stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(val)
                if token == '/':
                    val = stk[-2] / stk[-1]
                    stk.pop()
                    stk.pop()
                    stk.append(int(val))
            else:
                stk.append(int(token))
        return int(stk[-1])