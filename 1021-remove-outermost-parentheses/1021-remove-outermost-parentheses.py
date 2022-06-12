class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        summer = 0 
        listeraunt = []
        p=""
        for i,j in enumerate(s):
            if j =="(":
                summer += 1
            elif j == ")":
                summer -= 1
            if summer > 0:
                p += str(j)
            elif summer == 0:
                p += str(j)
                listeraunt.append(p)
                p=""
        a= ""
        for i in listeraunt:
            a = a + i[1:-1]
        return (a)