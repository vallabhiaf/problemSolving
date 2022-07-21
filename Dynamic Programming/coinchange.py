class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        #Bottom down approach
        #Dynamic Programming
         #Always visualize such problems iwth a desc tree
         
          dp=[amount+1]*(amount+1)
          dp[0]=0
        
          for i in range (1,amount+1):
                for c in coins:
                    if i-c>=0:
                        dp[i]=min(dp[i],1+dp[i-c])
           
          return dp[amount]  