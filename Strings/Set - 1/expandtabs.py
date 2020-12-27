"""
expandtabs() :- 
It is used to replace all tab characters(“\t”) with whitespace or simply spaces using the given tab size, which is optional to supply.

Syntax: string.tabsize(tabsize)

Parameters: Specifying the number of characters to be replaced for one tab character. By default, the function takes tab size as 8.

Return Value: A string in which all the tab characters are replaced with spaces.
"""

# Python code to illustrate expandtabs() 
string = 'GEEKS\tFOR\tGEEKS'

# No parameters, by default size is 8 
print (string.expandtabs()) 

# tab size taken as 2 
print(string.expandtabs(2)) 

# tab size taken as 5 
print(string.expandtabs(5)) 



"""

Output:

GEEKS   FOR     GEEKS
GEEKS FOR GEEKS
GEEKS     FOR  GEEKS

"""
