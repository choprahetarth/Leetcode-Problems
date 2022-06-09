class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        for i in range(len(nums)+1):
            if i==0:
                result = i
            else:
                result ^= i
        for j in nums:
            result ^= j
        return (result)