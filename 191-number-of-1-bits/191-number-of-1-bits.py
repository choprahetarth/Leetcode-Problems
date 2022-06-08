class Solution:
    def hammingWeight(self, n: int) -> int:
        a = str(bin(n))
        a = [x for x in a[2:] if x!='0']
        return len(a)