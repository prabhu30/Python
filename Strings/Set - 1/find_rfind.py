"""
find(“string”, beg, end) :- 
This function is used to find the position of the substring within a string.
It takes 3 arguments, substring , starting index( by default 0) and ending index( by default string length)

rfind(“string”, beg, end) :- 
This function has the similar working as find(), 
but it returns the position of the last occurrence of string.
"""

# Python code to demonstrate working of 
# find() and rfind() 
str = "geeksforgeeks is for geeks"
str2 = "geeks"

# using find() to find first occurrence of str2 
# returns 8 
print ("The first occurrence of str2 is at : ", end="") 
print (str.find( str2, 4) ) 

# using rfind() to find last occurrence of str2 
# returns 21 
print ("The last occurrence of str2 is at : ", end="") 
print ( str.rfind( str2, 4) ) 



"""
Output:

The first occurrence of str2 is at : 8
The last occurrence of str2 is at : 21
"""
