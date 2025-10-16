'''
Created on 16-Oct-2025

@author: mahim
Indentation: it is the leading space to define a block of code 
1 indentation = 1 tab space / 4 normal spaces
Conditional Statements: Flow of program execution will be decided based on a condition. 
Also called as decision making statements.

1.if statement 
2,if-else statement
3.series if-else statement
4.nested if-else

'''
age = int(input("Please enter your age:"))
'''
if age>12:
    #space is used here to define a block of code
    print("Age is satisfied")
else:
    print("Age is not satisfied")
  
print("Program terminated")
'''

if age>0:
    if age <=3:
        print("You're a toddler")
    elif age <=12:
        print("You're a child")
    elif age <=18:
        print("You're a teenager")
    elif age <=60:
        print("You're an adult")
    else:
        print("You're a senior citizen")
else:
    print("Please enter a positive number")