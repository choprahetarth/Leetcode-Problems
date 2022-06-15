class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        [nums1.append(x) for x in nums2]
        nums1.sort()
        print(nums1)
        length = len(nums1)
        if (length%2==0) :
            central_value1 = int(length/2)-1
            central_value2 = central_value1 +1
            return (nums1[central_value1] +nums1[central_value2])/2
        else:
            central_value1 = int(length/2)
            return nums1[central_value1]
            