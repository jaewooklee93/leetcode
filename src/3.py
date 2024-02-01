class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub, max_len = "", 0
        for x in s:
            i = sub.find(x)
            sub = (sub[i+1:] if i >= 0 else sub) + x
            max_len = max(max_len, len(sub))
        return max_len
    
print(Solution().lengthOfLongestSubstring("abcabcbb"))
        