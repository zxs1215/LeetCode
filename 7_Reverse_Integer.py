class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        sign = False
        if x < 0:
            sign = True
            x = -x
        s = str(x)
        s = s[::-1]
        n = int(s)
        if sign:
            n = -n
        if n > 2147483647 or n < -2147483648:
            return 0
        else:
            return n
        