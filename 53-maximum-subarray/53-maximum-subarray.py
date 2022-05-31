class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum_sum = 0
        current = 0
        if max(nums) < 0:
            return (max(nums))
        for i in range(len(nums)):
            current+=nums[i]
            if (current < 0):
                current = 0 
            if (maximum_sum < current):
                maximum_sum = current
        return maximum_sum
                
                