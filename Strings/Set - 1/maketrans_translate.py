"""
maketrans() :- 
It is used to map the contents of string 1 with string 2 with respective indices to be translated later using translate().

translate() :- 
This is used to swap the string elements mapped with the help of maketrans().
"""

# Python code to demonstrate working of 
# maketrans() and translate() 
from string import maketrans # for maketrans() 

str = "geeksforgeeks"

str1 = "gfo"
str2 = "abc"

# using maktrans() to map elements of str2 with str1 
mapped = maketrans( str1, str2 ) 

# using translate() to translate using the mapping 
print "The string after translation using mapped elements is : "
print str.translate(mapped) 



"""

Output :

The string after translation using mapped elements is : 
aeeksbcraeeks

"""
