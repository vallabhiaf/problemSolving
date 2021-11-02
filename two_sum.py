class Solution:
    def isPalindrome( s):
        t=""
        d=""
        
        for i in range(len(s)):
            if s[i].isalnum():
                 d = d+s[i]
        print(d)
        
        for i in range(len(s)-1,0,-1):
            if s[i].isalnum():
                 t = t+s[i]
        print(t)
        if t == d :
            return True
        else:
            return False

    result=isPalindrome("A man, a plan, a canal: Panama")
    print(result)