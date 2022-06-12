class Solution:
    def maxDepth(self, s: str) -> int:
        a = [x for x in s if x == ("(") or x== (")")]
        max_sum = 0 
        current_sum = 0
        print(a)
        for i,j in enumerate(a):
            if j == "(":
                current_sum += 1
            else :
                current_sum -= 1
            if max_sum < current_sum:
                max_sum = current_sum
            
        return max_sum
                