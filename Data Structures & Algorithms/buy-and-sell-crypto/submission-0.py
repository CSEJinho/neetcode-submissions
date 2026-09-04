class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprice = 0   
        while l < r and r < len(prices):
            if prices[l] < prices[r]:
                maxprice = max(maxprice, prices[r] - prices[l])
            else:
                l = r
            r += 1
        return maxprice
