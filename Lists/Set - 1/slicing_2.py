"""
Negative index list slicing :-
"""

# Creating a List 
List = ['G','E','E','K','S','F', 
		'O','R','G','E','E','K','S'] 
print("Initial List: ") 
print(List) 

# Print elements from beginning 
# to a pre-defined point using Slice 
Sliced_List = List[:-6] 
print("\nElements sliced till 6th element from last: ") 
print(Sliced_List) 

# Print elements of a range 
# using negative index List slicing 
Sliced_List = List[-6:-1] 
print("\nElements sliced from index -6 to -1") 
print(Sliced_List) 

# Printing elements in reverse 
# using Slice operation 
Sliced_List = List[::-1] 
print("\nPrinting List in reverse: ") 
print(Sliced_List) 



"""

Output:
Initial List: 
['G', 'E', 'E', 'K', 'S', 'F', 'O', 'R', 'G', 'E', 'E', 'K', 'S']

Elements sliced till 6th element from last: 
['G', 'E', 'E', 'K', 'S', 'F', 'O']

Elements sliced from index -6 to -1
['R', 'G', 'E', 'E', 'K']

Printing List in reverse: 
['S', 'K', 'E', 'E', 'G', 'R', 'O', 'F', 'S', 'K', 'E', 'E', 'G']

"""
