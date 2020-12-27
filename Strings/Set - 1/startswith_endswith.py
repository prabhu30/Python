"""
startswith(“string”, beg, end) :- 
The purpose of this function is to return true if the function begins with mentioned string(prefix) else return false.

endswith(“string”, beg, end) :- 
The purpose of this function is to return true if the function ends with mentioned string(suffix) else return false.
"""

# Python code to demonstrate working of 
# startswith() and endswith() 
str = "geeks"
str1 = "geeksforgeeksportal"

# using startswith() to find if str 
# starts with str1 
if str1.startswith(str): 
		print ("str1 begins with : " + str) 
else : print ("str1 does not begin with : "+ str) 

# using endswith() to find 
# if str ends with str1 
if str1.endswith(str): 
	print ("str1 ends with : " + str) 
else : 
	print ("str1 does not end with : " + str) 



"""

Output:

str1 begins with : geeks
str1 does not end with : geeks

"""
