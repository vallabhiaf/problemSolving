class Solution:
    def countSubstrings(self, s: str) -> int:
        
        res = 0

        #Plan for odd and even subscting bring palindrome by taking each character as middle element and expaniding both ways. 
        
        for i in range(len(s)):
            l=r=i
            while l>=0 and r < len(s) and s[l]== s[r]:
                l -=1
                r +=1
                res +=1
            
            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l]== s[r]:
                l -=1
                r +=1
                res +=1
                
        return res
            
                