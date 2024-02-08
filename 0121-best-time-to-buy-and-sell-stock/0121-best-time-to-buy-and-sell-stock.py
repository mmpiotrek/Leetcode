class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        itr = 0
        min_value = prices[0]
        max_value = 0
        max_profit = 0
        while itr < len(prices):
            if min_value < prices[itr]:
                max_value = max(max_value, prices[itr])
            else:
                max_value = 0
            min_value = min(min_value, prices[itr])
            profit = max_value - min_value
            max_profit = max(max_profit, profit)
            itr += 1
        return max_profit
        