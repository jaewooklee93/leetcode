from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major, cnt = nums[0], 1
        for n in nums[1:]:
            if n == major: cnt += 1
            elif cnt == 0: major, cnt = n, 1
            else: cnt -= 1
        return major
    
print(Solution().majorityElement([3,3,4])) # 3