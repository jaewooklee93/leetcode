from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """ Using Hashmap(dict): O(n) """
        mem = {}
        for i, num in enumerate(nums):
            if num in mem:
                return [mem[num], i] # mem[num] < i
            mem[target - num] = i

    def twoSum2(self, nums: List[int], target: int) -> List[int]:
        """ Using Two-Pointer: O(nlogn) """
        n = len(nums)
        nums = sorted((num, i) for i, num in enumerate(nums)) # O(nlogn)
        
        # search for (x, y), nums[x] + nums[y] == target
        # under 0 <= l <= x < y <= r < n
        l, r = 0, n-1
        while l < r: # O(n)
            d = nums[l][0] + nums[r][0] - target
            if d < 0: l += 1
            elif d > 0 : r -= 1
            else: return [nums[l][1], nums[r][1]]


def judge(fn):
    tests = [
        {
            "nums": [2, 7, 11, 15],
            "target": 9,
            "expected": [0, 1]
        },
        {
            "nums": [3, 2, 4],
            "target": 6,
            "expected": [1, 2]
        },
        {
            "nums": [3, 3],
            "target": 6,
            "expected": [0, 1]
        },
    ]
    print(fn.__name__)
    for t in tests:
        print(t)
        assert set(t.pop("expected")) == set(fn(**t))

if __name__ == "__main__":
    judge(Solution().twoSum)
    judge(Solution().twoSum2)