"""
len() :- 
This function returns the length of the string.

count(“string”, beg, end) :- 
This function counts the occurrence of mentioned substring in whole string. This function takes 
3 arguments, substring, beginning position( by default 0) and end position(by default string length).
"""

# Python code to demonstrate working of 
# len() and count() 
str = "geeksforgeeks is for geeks"

# Printing length of string using len() 
print (" The length of string is : ", len(str)); 

# Printing occurrence of "geeks" in string 
# Prints 2 as it only checks till 15th element 
print (" Number of appearance of ""geeks"" is : ",end="") 
print (str.count("geeks",0,15)) 



"""

Output :

The length of string is :  26
Number of appearance of geeks is : 2

"""
