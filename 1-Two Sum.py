class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = dict()
        for i in range(len(nums)):
            dic[i] = nums[i]
        tuples = sorted(dic.items(),key=lambda d: d[1])
        i,j = 0,-1
        start = tuples[i]
        end = tuples[j]
        while (start[1] + end[1] != target):
            if(start[1] + end[1] < target):
                i+=1
            else:
                j-=1
            start = tuples[i]
            end = tuples[j]
        index1 = start[0]+1
        index2 = end[0]+1
        return [index1,index2] if index1<index2 else [index2,index1]
        