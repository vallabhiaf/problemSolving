
 
# Function to remove all spaces from a given string
def removeSpaces(string):
 
    # To keep track of non-space character count
    count = 0
 
    list = []
 
    # Traverse the given string. If current character
    # is not space, then place it at index 'count++'
    for i in xrange(len(string)):
        if string[i] != ' ':
            list.append(string[i])
 
    return toString(list)
 
# Utility Function
def toString(List):
    return ''.join(List)
 
# Driver program
string1 = "g  eeks  for ge  eeks  "
print (removeSpaces(string1))

#We can use built in function replace
 