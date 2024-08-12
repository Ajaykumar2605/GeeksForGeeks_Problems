class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        m=nums1
        if len(m)%2==0:
            med=m[len(m)//2-1]+m[len(m)//2]
            n=float(med)/2
            return n
        else:
            return m[len(m)//2]
