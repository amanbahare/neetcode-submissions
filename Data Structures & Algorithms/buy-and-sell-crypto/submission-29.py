class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_buy= prices[0]
        max_profit = 0 
        for i in range(0, len(prices)):
            if prices[i] > best_buy :
                max_profit = max(max_profit, prices[i]-best_buy)
            best_buy = min(best_buy, prices[i])
        return max_profit
