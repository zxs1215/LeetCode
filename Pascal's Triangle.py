class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        list = []
        for i in range(1, numRows + 1):
            list.append(self.pascal(i))
        return list
        
    def pascal(self, n):
        if n == 1:
            return [1]
        prev = self.pascal(n - 1)
        list = [0] * n
        list[0] = 1
        list[n -1] = 1
        for i in range(n - 2):
            list[i + 1] = prev[i] + prev[i + 1]
        return list
        
sol = Solution()
sol.generate(4)