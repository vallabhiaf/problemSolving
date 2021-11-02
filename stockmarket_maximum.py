class Solution:
    def maxProfit(prices):
        smallest = prices[0]
        largest=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i] > largest:
                largest=prices[i]
            elif prices[i]< largest:
                profit=profit+(largest - smallest)
                smallest =prices[i]
                largest=prices[i]
        
        profit=profit+(largest-smallest)
        return profit
        