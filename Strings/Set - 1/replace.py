"""
replace() :- 
This function is used to replace the substring with a new substring in the string. This function has 3 arguments. 
The string to replace, new string which would replace and max value denoting the limit to replace action ( by default unlimited ).
"""

# Python code to demonstrate working of 
# replace() 

str = "nerdsfornerds is for nerds"

str1 = "nerds"
str2 = "geeks"

# using replace() to replace str2 with str1 in str 
# only changes 2 occurrences 
print ("The string after replacing strings is : ", end="") 
print (str.replace( str1, str2, 2)) 



"""

Output:

The string after replacing strings is : geeksforgeeks is for nerds

"""
