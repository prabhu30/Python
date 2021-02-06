s = "geeksforgeeks"
 
print("\nindex method :")
ind = s.index("g") #First occurence of "g"
print(ind)
ind = s.index("for")
print(ind)
# ind = s.index("gfg") ---> This raises index error, as gfg is not present in the string
 
print("\nisspace method :")
string = 'Geeksforgeeks'
print(string.isspace())
string = '\n \n \n'
print(string.isspace())
string = 'Geeks\nfor\ngeeks'
print( string.isspace())
 
print("\nswapcase method :")
string = "gEEksFORgeeks"
print(string.swapcase())
string = "striver"
print(string.swapcase())
 
print("\nreplace method :")
string = "geeks for geeks geeks geeks geeks"
# Prints the string by replacing geeks by Geeks 
print(string.replace("geeks", "Geeks"))
# Prints the string by replacing only 3 occurrence of Geeks 
print(string.replace("geeks", "GeeksforGeeks", 3))

"""
-------------------------------------------------------------------
OUTPUT :
index method :
0
5

isspace method :
False
True
False

swapcase method :
GeeKSforGEEKS
STRIVER

replace method :
Geeks for Geeks Geeks Geeks Geeks
GeeksforGeeks for GeeksforGeeks GeeksforGeeks geeks geeks



room
5th Floor, A-118,
Sector-136, Noida, Uttar Pradesh - 201305
email
feedback@geeksforgeeks.org
-------------------------------------------------------------------
"""