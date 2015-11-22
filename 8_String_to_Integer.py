import re
class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        value = 0
        s = re.match(r'^[-+]?\d*\d',str.strip())
        if s != None:
            value = int(s.group(0))
        value = min(value,2147483647)
        value = max(value,-2147483647 - 1)
        return value