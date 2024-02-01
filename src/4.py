class Solution:
    def merge(l1, l2):
        s = []
        while l1 and l2:
            if l1[0] < l2[0]: s.append(l1.pop(0))
            else: s.append(l2.pop(0))
        return s + l1 + l2
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        s = Solution.merge(nums1, nums2)
        d, m = divmod(len(s), 2)
        if m == 0: return (s[d-1] + s[d]) / 2
        else: return s[d]