'''
Created on 11-Oct-2025

@author: mahim

Variables: Name given to the container in a memory location which stores data(input/output)

Data stored in the location/container can be changed.

Syntax:

variable_name = value

Invalid cases:
1.While defining the variables ,Variable names should always be in left Hand Side and value should be in Right Hand Side.
2.Variable name should start with a character or letter. It should not start with numbers.
3.Numerical values should not start with 0.
4.
 
Comments: Which gives description about single line or block of a code

Types of Comments:
1.Single line comment, defined using #
2.Multi line comments, defined using triple single quotes / triple double quotes

'''
#Defining one variable at a time--> single line comment
num1 = 56
num2 = 34
num3 = 2+6j
name = "Mahima"# We can use single quotes as well
print(num1)
print(id(num1))
#Defining multiple variables in single line
num4,num5,num6 = 45, 67.8, 2+8j
print(num4)
print(num5)
print(num6)
print(id(num4))
print(id(num5))
print(id(num6))

num7 = num8 = 10
print(num7)
print(num8)
print(id(num7))
print(id(num8))

num8 =20
print(num8)
print(id(num8))
print(name)
print(id(name))

print(num7,num8)#printing multiple variables in one single print function
print("num7:", num7)