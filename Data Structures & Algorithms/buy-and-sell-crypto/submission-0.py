class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        lth = len(prices)
        for i,buy in enumerate(prices):
            res2 = 0
            for sell in prices[i+1:lth]:
                res1 = max(0,sell-buy)
                res2 = max(res2,res1)
            profit = max(profit,res2)
        return profit
            
            



        