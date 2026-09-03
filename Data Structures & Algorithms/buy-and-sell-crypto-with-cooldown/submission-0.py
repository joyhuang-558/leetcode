

'''
1. 状态定义
hold[i]:这天手上有股票
cash[i]:这天手上无股票

2. 转移方程
hold[i] = max(hold[i-1],cash[i-2]-price[i])
cash[i] = max(cash[i-1],hold[i-1]+price[i])
又因为，卖掉不能马上买
3. 初始value
cash[0]=0
cash[1]=max(0(说明前两天都没买)，price[1]-price[0](说明第二天卖掉，第一天买入))

hold[0]=-price[0]
hold[1]=max(-price[0],-price[1])

4. 返回结果
cash[len(prices)-1]

'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        len_p = len(prices)
        if len_p == 1:
            return 0
        
        hold = [0]*len_p
        cash = [0]*len_p
        
        cash[0]=0
        cash[1]=max(0,prices[1]-prices[0])
        hold[0]=-prices[0]
        hold[1]=max(-prices[0],-prices[1])

        for i in range(2,len_p):
            hold[i] = max(hold[i-1],cash[i-2]-prices[i])
            cash[i] = max(cash[i-1],hold[i-1]+prices[i])
        
        return cash[len_p-1]
        