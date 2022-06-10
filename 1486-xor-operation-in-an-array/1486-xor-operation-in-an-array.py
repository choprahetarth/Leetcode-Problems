class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        lister = list(range(start,start+2*(n),2))
        for i,j in enumerate(lister):
            print(i,j)
            if i == 0:
                start = j
            else:
                start ^= j
        
        return start
        # return 3^5^7