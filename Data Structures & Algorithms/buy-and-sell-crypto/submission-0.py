class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        curr = float("inf")
        for i in range(len(prices)):
            curr = min(prices[i],curr)
            profit = prices[i] - curr
            max_profit = max(max_profit,profit)
        
        return max_profit