class Solution:
    def isPalindrome(self, x: int) -> bool:
        if(x<0):
            return False
        reverse = 0 
        i = x
        while (i != 0):
            reverse = (reverse * 10) + (i % 10)
            i = i // 10
        if(x == reverse):
            return True
            
