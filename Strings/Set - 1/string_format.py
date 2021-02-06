print("1. ",end="")
print("{}, A computer science portal for geeks.".format("GeeksforGeeks"))

print("2. ",end="")
print("Hello, I am {} years old !".format(18))

print("3. ",end="")
print("{}, is a {} science portal for {}".format("GeeksforGeeks", "computer", "geeks"))

print("4. ",end="")
print("{0} love {1}!!".format("GeeksforGeeks","Geeks"))

print("5. ",end="")
print("{1} love {0}!!".format("GeeksforGeeks","Geeks"))

print("6. ",end="")
print("{gfg} is a {0} science portal for {1}".format("computer", "geeks", gfg ="GeeksforGeeks"))

# s – strings
# d – decimal integers (base-10)
# f – floating point display
# c – character
# b – binary
# o – octal
# x – hexadecimal with lowercase letters after 9
# X – hexadecimal with uppercase letters after 9
# e – exponent notation

# Convert base-10 decimal integers 
# to floating point numeric constants 
print("7. ",end="")
print ("This site is {0:f}% securely {1}!!".format(100, "encrypted"))

# To limit the precision 
print("8. ",end="")
print ("My average of this {0} was {1:.2f}%".format("semester", 78.234876))

# For no decimal places 
print("9. ",end="")
print ("My average of this {0} was {1:.0f}%".format("semester", 78.234876))

# Convert an integer to its binary or 
# with other different converted bases. 
print("10. ",end="")
print("The {0} of 100 is {1:b}".format("binary", 100))

print("11. ",end="")
print("The {0} of 100 is {1:o}".format("octal", 100))

"""
By default strings are left-justified within the field, and numbers are right-justified. 
We can modify this by placing an alignment code just following the colon.

<   :  left-align text in the field
^   :  center text in the field
>   :  right-align text in the field
"""

# To demonstrate spacing when 
# strings are passed as parameters 
print("12. ",end="")
print("{0:4}, is the computer science portal for {1:8}!".format("GeeksforGeeks", "geeks"))

# To demonstrate spacing when numeric 
# constants are passed as parameters. 
print("13. ",end="")
print("It is {0:5} degrees outside !".format(40))

# To demonstrate both string and numeric 
# constants passed as parameters 
print("14. ",end="")
print("{0:4} was founded in {1:16}!".format("GeeksforGeeks", 2009))

# To demonstrate aligning of spaces 
print("15. ",end="")
print("{0:^16} was founded in {1:<4}!".format("GeeksforGeeks", 2009))

print("16. ",end="")
print("{:*^20s}".format("Geeks"))







"""
-------------------------------------------------------------------------------------------------------------
OUTPUT :
1. GeeksforGeeks, A computer science portal for geeks.
2. Hello, I am 18 years old !
3. GeeksforGeeks, is a computer science portal for geeks
4. GeeksforGeeks love Geeks!!
5. Geeks love GeeksforGeeks!!
6. GeeksforGeeks is a computer science portal for geeks
7. This site is 100.000000% securely encrypted!!
8. My average of this semester was 78.23%
9. My average of this semester was 78%
10. The binary of 100 is 1100100
11. The octal of 100 is 144
12. GeeksforGeeks, is the computer science portal for geeks   !
13. It is    40 degrees outside !
14. GeeksforGeeks was founded in             2009!
15.  GeeksforGeeks   was founded in 2009!
16. *******Geeks********
-------------------------------------------------------------------------------------------------------------
"""
