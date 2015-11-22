class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        upper = string.uppercase
        num = range(26)
        dic = {}
        for i in num:
            dic[upper[i]] = i 
        result = 0 
        for c in s:
            result = result * 26 + dic[c] + 1
        return result