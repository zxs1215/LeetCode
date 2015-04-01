class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        bitstr = bin(n)[2:]
        length = len(bitstr)
        if length < 32:
            bitstr = '0' * (32 - length) + bitstr
        result = 0
        for bit in bitstr[::-1]:
            result *= 2
            result += int(bit)
        return result