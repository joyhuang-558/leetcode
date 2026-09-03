class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        right = left = 0
        res = 0
        while right < len(prices):
            if prices[left]>prices[right]:
                left = right
            else:
                res = max(res,prices[right]-prices[left])
            right += 1
        return res

             

        