"""
lower() :- 
This function returns the new string with all the letters converted into its lower case.

upper() :- 
This function returns the new string with all the letters converted into its upper case.

swapcase() :- 
This function is used to swap the cases of string i.e upper case is converted to lower case and vice versa.

title() :- 
This function converts the string to its title case i.e the first letter of every word of string is upper cased and else all are lower cased.
"""

# Python code to demonstrate working of 
# upper(), lower(), swapcase() and title() 
str = "GeeksForGeeks is fOr GeeKs"

# Coverting string into its lower case 
str1 = str.lower(); 
print (" The lower case converted string is : " + str1) 

# Coverting string into its upper case 
str2 = str.upper(); 
print (" The upper case converted string is : " + str2) 

# Coverting string into its swapped case 
str3 = str.swapcase(); 
print (" The swap case converted string is : " + str3) 

# Coverting string into its title case 
str4 = str.title(); 
print (" The title case converted string is : " + str4) 



"""

Output:

The lower case converted string is : geeksforgeeks is for geeks
The upper case converted string is : GEEKSFORGEEKS IS FOR GEEKS
The swap case converted string is : gEEKSfORgEEKS IS FoR gEEkS
The title case converted string is : Geeksforgeeks Is For Geeks

"""
