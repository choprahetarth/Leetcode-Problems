class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = len(nums1)
        b = len(nums2)
        if a >b:
            smaller_array = nums2
            larger_array = nums1
        else:
            smaller_array = nums1
            larger_array = nums2
        return_arr =[]
        for i in smaller_array:
            if i in larger_array:
                return_arr.append(i)
                larger_array.remove(i)
        return return_arr
        