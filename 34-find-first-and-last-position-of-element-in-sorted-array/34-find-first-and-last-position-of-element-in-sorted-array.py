class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        try:
            nums.sort()
            start = nums.index(target)
            nums.sort(reverse=True)
            end = len(nums)-1-nums.index(target)
            return ([start,end])
        except:
            return([-1,-1])
        
        
           
            