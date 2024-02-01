from collections import deque as stack

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = stack()
        for token in tokens:
            if token in "+-*/":
                b, a = s.pop(), s.pop()
                match token:
                    case "+": s.append(a+b)
                    case "-": s.append(a-b)
                    case "*": s.append(a*b)
                    case "/": s.append(a//b)
            else:
                s.append(int(token))
        return s.pop()