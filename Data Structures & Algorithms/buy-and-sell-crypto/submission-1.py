class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # O(n) solution
        min_price = prices[0]
        max_profit = 0

        for price in prices:

            profit = price - min_price

            # 1. Is this the best profit we've seen?
            if profit > max_profit:
                max_profit = profit

            # 2. Is today's price cheaper than our current min_price?
            if min_price > price: 
                min_price = price 
        return max_profit

