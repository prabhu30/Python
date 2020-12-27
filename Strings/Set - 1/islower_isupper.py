"""
islower(“string”) :- 
This function returns true if all the letters in the string are lower cased, otherwise false.

isupper(“string”) :- 
This function returns true if all the letters in the string are upper cased, otherwise false.
"""

# Python code to demonstrate working of 
# isupper() and islower() 
str = "GeeksforGeeks"
str1 = "geeks"

# checking if all characters in str are upper cased 
if str.isupper() : 
	print ("All characters in str are upper cased") 
else : 
	print ("All characters in str are not upper cased") 

# checking if all characters in str1 are lower cased 
if str1.islower() : 
	print ("All characters in str1 are lower cased") 
else : 
	print ("All characters in str1 are not lower cased") 



"""

Output:

All characters in str are not upper cased
All characters in str1 are lower cased

"""
