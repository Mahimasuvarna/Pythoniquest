'''
Created on 14-Oct-2025

@author: mahim

Operator: Is a symbol which performs operation on one or more operands(variables)

Classification of operators based on No.of operands:
1.Unary operator-acts on a single variable/value( =,-)
2.Binary Operator: acts on two variables/values(+,-,*...etc)
3.Ternary Operator:acts on three operands(list comprehension)

Classification of operators based on operations

1.Arithmetic Operators:+,-,*,/(quotient),%(reminder),**(exponent),//(floor division)
2.Comparison Operators/Relational Operators:>,<,<=,>=,!=,==
i/p = numerical and o/p is boolean..
3.Assignment Operator:=
4.Logical Operator:AND,OR,NOT
5.Membership Operators:To check whether any element is part of a group ---in,not in
6.Identity Operators :To check identity / to check whether 2 variables are identical --is, is not
7.Unary Minus Operator: To negate the numbers
'''
from pickle import FALSE
from _operator import or_

print("=========Arithmetic Operators=======")
a = 20
b = 3
print("a+b:", a+b)
print("a-b:",a-b)
print("a*b:",a*b)
print("a/b:",a/b)
print("a%b:",a%b)
print("a//b:",a/b)
print("20.0//3:",20.0//3)

print("=======Comparison Operators=====")
print("a>b:",a>b)
print("a<b:",a<b)
print("a>=b:",a>=b)
print("a<=b:",a<=b)
print("a==b:",a==b)
print("a!=b:",a!=b)

print("=========Logical Operators=======")
print("=========AND Operator=======")
print("True and True:", True and True)
print("True and False:", True and False)
print("False and True:", False and True)
print("False and False:", False and False)

print("=========OR Operator=======")
print("True or True:", True or True)
print("True or False:", True or False)
print("False or True:", False or True)
print("False or False:", False or False)

print("=========Not Operator=======")
print("Not true:", not True)
print("Not false", not False)

print("========Membership Operator=====")
print("'i' in 'mahima'",'i' in 'mahima')
print("'I' in 'mahima'",'I' in 'mahima')
print("'x' in 'mahima'",'x' in 'mahima')
print("'x' not in 'mahima'",'x' not in 'mahima')

print("======Identity Operators=====")
name1 = 'Vivek'
name2 = 'vivek'
print(id(name1))
print(id(name2))
print("name1 is name2:" , name1 is name2)
print("name1 is not name:", name1 is not name2)
#print("'Vivek' is 'vivek:", 'Vivek' is 'vivek')
#print("'Vivek' is not 'vivek:", 'Vivek' is not 'vivek')
