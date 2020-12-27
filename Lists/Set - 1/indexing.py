"""
In order to access the list items refer to the index number.Use the index operator [ ] to access an item in a list.
The index must be an integer.Nested list are accessed using nested indexing.
"""

# Python program to demonstrate 
# accessing of element from list 

# Creating a List with 
# the use of multiple values 
List = ["Geeks", "For", "Geeks"] 

# accessing a element from the 
# list using index number 
print("Accessing a element from the list") 
print(List[0]) 
print(List[2]) 

# Creating a Multi-Dimensional List 
# (By Nesting a list inside a List) 
List = [['Geeks', 'For'] , ['Geeks']] 

# accessing an element from the 
# Multi-Dimensional List using 
# index number 
print("Acessing a element from a Multi-Dimensional list") 
print(List[0][1]) 
print(List[1][0]) 



"""

Output:
Accessing a element from the list
Geeks
Geeks
Acessing a element from a Multi-Dimensional list
For
Geeks

"""
