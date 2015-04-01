class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        binnum = bin(n)[2:]
        count = 0
        for i in binnum:
            if i == '1':
                count += 1
        
        return count    