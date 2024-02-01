from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        s = sum(nums[:3])
        if s >= target: return s
        min_dist = s - target
        if sum(nums[-3:]) <= target: return sum(nums[-3:])
        for i, ni in enumerate(nums):
            if sum(nums[i:i+3]) > target + abs(min_dist): 
                return target + min_dist
            if i != 0 and ni == nums[i-1]: continue
            
            l, r = i+1, len(nums)-1
            _d = ni - target
            while l < r:
                d = nums[l] + nums[r] + _d
                if abs(d) < abs(min_dist):
                    min_dist = d
                if d > 0: r -= 1
                elif d < 0: l += 1
                else: return target
        return target + min_dist
    
print(Solution().threeSumClosest(nums = [-1,2,1,-4], target = 1))