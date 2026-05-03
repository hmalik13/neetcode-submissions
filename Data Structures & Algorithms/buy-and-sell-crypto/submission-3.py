class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        # buy low, sell high
        while sell < len(prices):
            # if buy is less than sell, we have a profit
            if prices[buy] < prices[sell]:
                profit = prices[sell] - prices[buy]
                max_profit = max(profit, max_profit)
            # if buy is not less than sell,
            # then sell becomes the next best buy
            # we only want to increment this pointer
            # if we know another value is lower
            else:
                buy = sell
            sell += 1
        return max_profit
            

