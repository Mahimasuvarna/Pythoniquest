'''
Created on 19-Oct-2025

@author: mahim
'''
'''
print("====Program to check whether number is positive or not====")
num=int(input("Please enter a number:"))
if num < 0:
    print("The number is negative")
elif num == 0:
    print("The number is 0")
else:
    print("The number is positive")
 
print("====Program to check greatest of three numbers=====")
a=int(input("Please enter the first number:"))
b=int(input("Please enter the second number:"))
c=int(input("Please enter the third number"))
if a>b and a>c:
    print("a is greatest number")
elif b>a and b>c:
    print("b is greatest number")
else:
    print("c is greatest number")
 
 
print("=====student marks grade system=====")
marks=int(input("Enter the marks obtained:"))
if marks>=90:
    print("Grade is : A+")
elif marks>=80 and marks<=89:
    print("Grade is : A")
elif marks>=70 and marks<=79:
    print("Grade is : B")
else:
    print("Grade is: C")
    
    
    
print("======even or odd number======")
num2 = int(input("Enter a number:"))
if num2 % 2 == 0:
    print("Even number")
else:
    print("Odd number")   
   
 '''  
 
   
print("=====Number is divisible by 3 & 5=======")
num3 = int(input("Enter a number:"))
if num3 % 3 == 0 and num3 % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number not divisible by both 3 and 5")