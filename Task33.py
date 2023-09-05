class Solution:
    def maxProfit(self, prices):
        profit = -prices[0]
        buy_day = 0
        for cur_pos in range(0, len(prices) - 1):
            print(profit)
            if prices[cur_pos] > prices[cur_pos + 1] and buy_day != -1:
                profit += prices[cur_pos]
                buy_day = -1
            elif prices[cur_pos] < prices[cur_pos + 1] and buy_day == -1:
                buy_day = cur_pos
                profit -= prices[cur_pos]
        if buy_day != -1:
            profit += prices[-1]

        return profit
