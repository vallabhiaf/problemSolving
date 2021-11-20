class Solution:
    def lengthOfLongestSubstring(s):
        setmax=set() #Data strucutre can only contain unique chars 
        maxi=0
        left=0
        
        for r in range (len(s)):
            while s[r] in setmax:
                setmax.remove(s[left])
                left +=1
            setmax.add(s[r])
            maxi=max(maxi,(r-left +1))
            
        return maxi

    result=lengthOfLongestSubstring("pwwkew")
    print (result)