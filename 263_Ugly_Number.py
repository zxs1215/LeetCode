"""

Ugly Number 

Write a program to check whether a given number is an ugly number.

Ugly numbers are positive numbers whose prime factors only include 2, 3, 5. For example, 6, 8 are ugly while 14 is not ugly since it includes another prime factor 7.

Note that 1 is typically treated as an ugly number.

Credits:
Special thanks to @jianchao.li.fighter for adding this problem and creating all test cases.

Subscribe to see which companies asked this question

"""

class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num == 1:
            return True
        if num <= 0:
            return False
        ugly_nums = [2,3,5]
        for ugly in ugly_nums:
            num = self.divide_num(ugly, num)
        return num == 1
        
    def divide_num(self, prime, num):
        if num % prime == 0:
            num /= prime
            return self.divide_num(prime, num)
        return num
