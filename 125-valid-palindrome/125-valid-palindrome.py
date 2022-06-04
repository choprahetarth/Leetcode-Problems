class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        a = [x for x in s if x.isalnum()]
        b = a.copy()
        a.reverse()
        # print(a)
        if a == b :
            return True            