# import math
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = []
        temp = []
        for i in range(0, len(prices)):
            if prices[i] not in temp:
                temp.append(prices[i])
                for j in range(i+1, len(prices)):
                    if prices[i] < prices[j] :
                        profit.append(prices[j]-prices[i])
                        print("profit :", profit)
        if len(profit) == 0 :
            max_profit = 0
        else :
            max_profit = max(profit)
        return max_profit