#题目根本没说k大于数组长度的情况该怎么做简直坑爹
class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        length = len(nums)
        if k >= length:
            k %= length
        l1 = nums[length - k:]
        #print(l1)
        for i in range(k, length)[::-1]:
            nums[i] = nums[i - k]
        #print(nums)
        for i in range(k):
            nums[i] = l1[i]  
        #print(nums)

#Test
so = Solution()
nums = [1,2,3]

so.rotate(nums, 1)
input()