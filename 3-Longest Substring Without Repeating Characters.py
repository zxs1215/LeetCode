class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = dict()
        length = 0
        l = 0
        for r in range(len(s)):
            if s[r] in dic and dic[s[r]] >= l:
                l = dic[s[r]] + 1
            dic[s[r]] = r
            length = max(length, r-l+1)
        return length

s = Solution()
a = s.lengthOfLongestSubstring("abcabcaabb")
print a