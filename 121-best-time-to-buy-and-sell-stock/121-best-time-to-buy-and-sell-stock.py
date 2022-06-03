class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_price = float('inf')
        for i in prices:
            if i < min_price:
                min_price = i
            if i - min_price > profit:
                profit = i-min_price
        return profit