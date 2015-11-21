class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result = [True]*3 + [False]
        return result[(n-1)%4]
