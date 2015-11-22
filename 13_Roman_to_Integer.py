class Solution:
    # @param {string} s
    # @return {integer}
    def romanToInt(self, s):
        chs = ['I','V','X','L','C','D','M'] 
        nums = [1,5,10,50,100,500,1000]
        prev_index = None 
        prev_val = 0;
        result = 0
        for c in s:
            if not c in chs:
                return 0
            now_index = chs.index(c)
            now = nums[now_index]
            if prev_index == None:
                prev_val = now
                prev_index = now_index
                continue
            if (now_index - prev_index) in range(1,3):
                result += now - prev_val
                prev_val = 0
            elif now_index == prev_index:
                prev_val += now
            elif now_index > prev_index:
                result += now + prev_val
                prev_val = 0
            else:
                result += prev_val
                prev_val = now
            prev_index = now_index
        if prev_val != 0:
            result += prev_val    
        return result