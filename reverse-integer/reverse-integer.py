class Solution:
    def reverse(self, x: int) -> int:
        if x == 0:
            return 0
        else : 
            sign = abs(x)/x
            x = abs(x)
            x = list(str(x))
            reverse = []
            reverse_str = ""
            for i in range(len(x)):
                reverse.append(x[-i-1])
            reverse_str = reverse_str.join(reverse)
            reverse = int(reverse_str)*int(sign)
            if (reverse > (pow(2,31)-1) or reverse < (pow(-2,31))):
                reverse = 0
            return reverse
    