class Solution:
    def reverseBits(self, n: int) -> int:
        a = bin(n)
        a = a[2:]
        a = [x for x in a]
        a.reverse()
        a = "".join(a)
        while len(a)!=32:
            a+='0'
        # print(a)
        return int(a,2)
        
        