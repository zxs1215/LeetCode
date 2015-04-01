class Solution:
    # @param prices, a list of integer
    # @return an integer
    def maxProfit(self, prices):
        benifit = 0
        if len(prices) < 1:
            return 0
        start = prices[0]
        for price in prices[1:]:
            if price - start > 0:
                benifit += price - start
            start = price
        return benifit