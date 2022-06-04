class Solution:
    def isPalindrome(self, x: int) -> bool:
        _string = str(x)
        _string = [x for x in _string]
        a = _string.copy()
        _string.reverse()
        if a == _string:
            return True