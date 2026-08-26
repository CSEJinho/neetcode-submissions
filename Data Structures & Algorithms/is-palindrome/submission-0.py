class Solution:
    def isPalindrome(self, s: str) -> bool:
        deleted_s = []
        for w in s:
            if w.isalnum(): 
                deleted_s.append(w.lower())
        flag = True
        for i in range(len(deleted_s)):
            if deleted_s[i] != deleted_s[len(deleted_s) - i - 1]:
                flag = False
        return flag
