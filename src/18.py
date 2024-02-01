from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        if sum(nums[-4:]) < target: return []
        ans = []
        for i, ni in enumerate(nums):
            if sum(nums[i:i+4]) > target: break
            if i != 0 and ni == nums[i-1]: continue
            if ni + sum(nums[-3:]) < target: continue
            for j in range(i+1, len(nums)):
                nj = nums[j]
                if ni + sum(nums[j:j+3]) > target: break
                if j != i+1 and nj == nums[j-1]: continue
                l, r = j+1, len(nums)-1
                _d = target - ni - nj
                while l < r:
                    d = nums[l] + nums[r]
                    if d > _d: r -= 1
                    elif d < _d: l += 1
                    else: 
                        ans.append([ni, nj, nums[l], nums[r]])
                        l, r = l+1, r-1
                        while l < r and nums[l-1] == nums[l]: l += 1
                        while l < r and nums[r+1] == nums[r]: r -= 1
        return ans
print(Solution().fourSum([2,2,2,2,2], 8))