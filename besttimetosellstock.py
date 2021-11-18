class Solution:
    def maxProfit(prices):
        if len(prices) == 1 or len(prices) == 0:
             return 0
        l=0 #buy
        r=1 #sell
        maxProfit=0
        profit=0
      
        while r < len(prices):
            prices[l]
            prices[r]
            if prices[l] < prices[r]:
                profit= prices[r]-prices[l]
                maxProfit=max(maxProfit,profit)
            else:
                l =r
            r +=1
            
        return maxProfit
    
    answer=maxProfit([7,1,5,3,6,4])