class Solution:
    def fib(self, n: int) -> int:
        def rec_fib(n):
            if n == 0 :
                return 0
            elif n == 1:
                return 1
            else :
                return rec_fib(n-2)+rec_fib(n-1)
        return rec_fib(n)