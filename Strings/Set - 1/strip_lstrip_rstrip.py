"""
strip() :- 
This method is used to delete all the leading and trailing characters mentioned in its argument.

lstrip() :- 
This method is used to delete all the leading characters mentioned in its argument.

rstrip() :- 
This method is used to delete all the trailing characters mentioned in its argument.
"""

# Python code to demonstrate working of 
# strip(), lstrip() and rstrip() 
str = "---geeksforgeeks---"

# using strip() to delete all '-' 
print ( " String after stripping all '-' is : ", end="") 
print ( str.strip('-') ) 

# using lstrip() to delete all trailing '-' 
print ( " String after stripping all leading '-' is : ", end="") 
print ( str.lstrip('-') ) 

# using rstrip() to delete all leading '-' 
print ( " String after stripping all trailing '-' is : ", end="") 
print ( str.rstrip('-') ) 


"""

Output:

 String after stripping all '-' is : geeksforgeeks
 String after stripping all leading '-' is : geeksforgeeks---
 String after stripping all trailing '-' is : ---geeksforgeeks

"""
