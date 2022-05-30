class Solution:
    def climbStairs(self, n: int) -> int:
        a = list(range(1,n+1))
        b = [1,1]
        def add_new(lister):
            if len(lister)<=n:
                lister.append(lister[-1]+lister[-2])
                return add_new(lister)
            else:
                return(lister[-1])
        c = add_new(b)
        return (c)

