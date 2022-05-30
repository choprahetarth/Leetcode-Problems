class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        search_set = set(nums)
        count = 0
        retrn_elemnt = 0
        for i in search_set:
            instances = [j for j,x in enumerate(nums) if x == i]
            if len(instances)>count:
                count = len(instances)
                retrn_elemnt = i
        return retrn_elemnt
        