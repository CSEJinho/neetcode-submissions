class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        num_ch = dict()
        for ch in s:
            if ch in num_ch.keys():
                num_ch[ch] += 1 
            else:
                num_ch[ch] = 1
        for ch in t:
            if ch in num_ch:
                num_ch[ch] -= 1
            else:
                return False
        for num in num_ch.values():
            if num != 0: 
                return False
        return True
    