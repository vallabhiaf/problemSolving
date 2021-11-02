class Solution:
    def longestCommonPrefix( strs):
        n=len(strs)
        prefix=strs[0]
        for i in range(1,n):
            l=len(prefix)
            s=len(strs[i])
            counter=0
            prefixf=""
            while s>0 and l>0:
                if prefix[counter]== strs[i][counter]:
                    
                    s -=1
                    l -=1
                    prefixf=prefixf+prefix[counter]
                    counter +=1
                else:
                    prefix=prefixf
                    break
            prefix=prefixf
        return prefix
    strs=["dog","racecar","car"]              
    RESULT= longestCommonPrefix(strs)
    print(RESULT)
               