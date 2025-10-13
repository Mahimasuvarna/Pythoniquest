'''
Created on 13-Oct-2025

@author: mahim

Data types:

type() --> Pre-defined function to determine the type of data stored in variables

Built-in data types in Python:

Fundamental data types:
1.Numerical data types:
   -int
   -float
   -complex
2.String-str
3.Boolean - True or False
4.None
5.Bytes[not used]
6.Bytearray[not used]

Derived data types/ Data-structures:
   1.list
   2.Tuple
   3.Set
   4.Dictionary
   
Type Casting: Conversion of one data-type to another data-type
This can be achieved using built-in functions :
1.int()-converts one data-type to integer datatype
2.float()-converts to float data-type
3.complex()-converts to complex data-type
4.bool()-converts to boolean data-type
5.str()-converts to string data-type 

'''
num1 = 23 # int
num2 = 34.5#float
num3 = 4+5j#complex
name = 'Mahima'#str
var1 = True #boolean
var2 = False #boolean
var3 = None #Nonetype when we need to define a variable without a value initially

print("Type of num1:",type(num1))
print("Type of num2:",type(num2))
print("Type of num3:",type(num3))
print("Type of name:",type(name))
print("Type of var1:",type(var1))
print("Type of var2:",type(var2))
print("Type of var3:",type(None))


print("======Converting int to other data-types=======")
print('num1:', num1)
num4 = float(num1)
print('num4:',num4)
print(type(num4))

num5 = complex(num1)
print('num5:',num5)
print(type(num5))

num6 = str(num1)
print('num6:',num6)
print(type(num6))

num7 = bool(num1)
print('num7:',num7)
print(type(num7))

num8 = 0
num9 = bool(num8)
print('num9:',num9)
print(type(num9))


print("======Converting float to other data-types=======")
print('num2:', num2)
num10 = int(num2)
print('num10:',num10)
print(type(num10))

num11 = complex(num2)
print('num11:',num11)
print(type(num11))

num12 = str(num2)
print('num12:',num12)
print(type(num12))

num13 = bool(num2)
print('num13:',num13)
print(type(num13))


print("======Converting complex to other data-types=======")
print('num3:', num3)
'''
num14= int(num3)# TypeError: int() argument must be a string, a bytes-like object or a real number, not 'complex'

print('num14:',num14)
print(type(num14))
'''
'''
num15 = float(num3)#TypeError: float() argument must be a string or a real number, not 'complex'

print('num15:',num15)
print(type(num15))
'''
num16 = str(num3)
print('num16:',num16)
print(type(num16))

num17 = bool(num3)
print('num17:',num17)
print(type(num17))

print("======Converting str to other data-types=======")
print('name:', name)
'''
name1 = int(name)#ValueError: invalid literal for int() with base 10: 'Mahima'
print('name1:',name1)
print(type(name1))

name2 = float(name)# ValueError: could not convert string to float: 'Mahima'
print('name2:',name2)
print(type(name2))

name3 = complex(name)#ValueError: complex() arg is a malformed string
print('name3:',name3)
print(type(name3))
'''
name4 = bool(name)
print('name4:',name4)
print(type(name4))


print("======Converting boolean to other data-types=======")
print('var1:', var1)
var3 = int(var1)
print('var3:',var3)
print(type(var3))

var4 = complex(var1)
print('var4:',var4)
print(type(var4))

var5 = str(var1)
print('var5:',var5)
print(type(var5))

var6 = float(var1)
print('var6:',var6)
print(type(var6))



