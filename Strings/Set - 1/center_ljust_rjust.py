"""
center() :- 
This function is used to surround the string with a character repeated both sides of string multiple times. 
By default the character is a space. Takes 2 arguments, length of string and the character.

ljust() :- 
This function returns the original string shifted to left that has a character at its right. 
It left adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.

rjust() :- 
This function returns the original string shifted to right that has a character at its left. 
It right adjusts the string. By default the character is space. It also takes two arguments, length of string and the character.
"""

# Python code to demonstrate working of 
# center(), ljust() and rjust() 
str = "geeksforgeeks"

# Printing the string after centering with '-' 
print ("The string after centering with '-' is : ",end="") 
print ( str.center(20,'-')) 

# Printing the string after ljust() 
print ("The string after ljust is : ",end="") 
print ( str.ljust(20,'-')) 

# Printing the string after rjust() 
print ("The string after rjust is : ",end="") 
print ( str.rjust(20,'-')) 



"""

Output:

The string after centering with '-' is : ---geeksforgeeks----
The string after ljust is : geeksforgeeks-------
The string after rjust is : -------geeksforgeeks

"""
