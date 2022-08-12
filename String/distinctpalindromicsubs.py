class Solution:
    def countdistinctSubstrings(s):
        
        res = 0
        res1=[]

        #Plan for odd and even subscting bring palindrome by taking each character as middle element and expaniding both ways. 
        
        for i in range(len(s)):
            l=r=i
            while l>=0 and r < len(s) and s[l]== s[r]:
                sub=s[l:r+1]
                if sub not in res1:
                    res +=1
                    res1.append(sub)
                l -=1
                r +=1
                



            l=i
            r=i+1
            while l>=0 and r < len(s) and s[l]== s[r]:
                sub=s[l:r+1]
                if sub not in res1:
                    res +=1
                    res1.append(sub)
                l -=1
                r +=1
                
                
        return res


    
    res=countdistinctSubstrings("aaa")
    print(res)

            
                