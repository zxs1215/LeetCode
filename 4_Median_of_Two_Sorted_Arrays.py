class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1, l2 = len(nums1), len(nums2)
        median = (l1 + l2)/2 + 1
        addout = []
        while (len(addout) < median):
            if (nums2 == []):
                addout += [nums1[0]]
                del nums1[0]
            elif (nums1 == [] or nums1[0] > nums2[0]):
                addout += [nums2[0]]
                del nums2[0]
            else:
                addout += [nums1[0]]
                del nums1[0]
        if (l1+l2) % 2 == 0:
            return (addout[-1] + addout[-2]) / 2.0
        else:
            return addout[-1];