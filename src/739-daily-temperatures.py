from typing import List

from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = deque()

        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans

def judge(fn):
    tests = [
        {
            "temperatures": [73,74,75,71,69,72,76,73],
            "expected": [1,1,4,2,1,1,0,0]
        },
        {
            "temperatures": [30,40,50,60],
            "expected": [1,1,1,0]
        },
        {
            "temperatures": [30,60,90],
            "expected": [1,1,0]
        },
    ]
    print(fn.__name__)
    for t in tests:
        print(t)
        assert t.pop("expected") == fn(**t)

if __name__ == "__main__":
    judge(Solution().dailyTemperatures)