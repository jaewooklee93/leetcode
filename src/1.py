class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = sorted([(x, i) for i, x in enumerate(nums)])
        l, r = 0, len(nums)-1
        while l < r:
            d = nums[l][0] + nums[r][0] - target
            if d > 0: r -= 1
            elif d < 0: l += 1
            else: return [nums[l][1], nums[r][1]]