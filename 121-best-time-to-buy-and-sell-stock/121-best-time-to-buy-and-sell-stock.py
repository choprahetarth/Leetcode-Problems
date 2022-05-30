class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        for i in range(len(prices)):
            if min_price > prices[i]:
                min_price = prices[i]
            elif (prices[i] - min_price) > profit:
                profit = prices[i] - min_price
        return profit
            