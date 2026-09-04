class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        apla = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in apla:
                apla.remove(s[l])
                l += 1
            apla.add(s[r])
            res = max(res, len(apla))
        return res