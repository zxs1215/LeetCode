class Solution(object):
    def getRow(self, index):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        row = [1]
        for x in range(index):
            row = self.next_triangle(row)
        return row
        
    def next_triangle(self,last):
        lenth = len(last)
        result = [1]*(lenth+1)
        for i in range(lenth-1):
            result[i+1] = last[i]+last[i+1]
        return result
        