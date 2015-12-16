class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        eqs = filter(lambda x:x==val, nums)
        for i in range(len(eqs)):
            nums.remove(val)
        return len(nums)