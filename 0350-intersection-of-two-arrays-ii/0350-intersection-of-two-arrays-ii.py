class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        if len(nums2)<len(nums1):
            nums1,nums2 = nums2,nums1
        c1 = Counter(nums1)
        res = []
        for num in nums2:
            if c1[num]>0:
                res.append(num)
                c1[num]-=1
        return res
        