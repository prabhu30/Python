"""
isalpha() :- 
This function returns true when all the characters in the string are alphabets else returns false.

isalnum() :- 
This function returns true when all the characters in the string are combination of numbers and/or alphabets else returns false.

isspace() :- 
This function returns true when all the characters in the string are spaces else returns false.
"""

# Python code to demonstrate working of 
# isalpha(), isalnum(), isspace() 
str = "geeksforgeeks"
str1 = "123"

# Checking if str has all alphabets 
if (str.isalpha()): 
	print ("All characters are alphabets in str") 
else : print ("All characters are not alphabets in str") 

# Checking if str1 has all numbers 
if (str1.isalnum()): 
	print ("All characters are numbers in str1") 
else : print ("All characters are not numbers in str1") 

# Checking if str1 has all spaces 
if (str1.isspace()): 
	print ("All characters are spaces in str1") 
else : print ("All characters are not spaces in str1") 


"""

Output:

All characters are alphabets in str
All characters are numbers in str1
All characters are not spaces in str1

"""
