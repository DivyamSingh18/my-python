a = 5 
b = "7"

result = a+b    # throws error 

result = a+int(b)
print(result)    # o/p > 12

# typecasting to integer:
x = int(1)   # x will be 1
y = int(2.8) # y will be 2
z = int("3") # z will be 3

# typecasting to float:
x = float(1)     # x will be 1.0
y = float(2.8)   # y will be 2.8
z = float("3")   # z will be 3.0
w = float("4.2") # w will be 4.2

'''
the conversion of one data type into the other data type is known as type casting in python or type conversion in python. Python supports a wide
variety of functions or methods like: int(), float(), str(), ord(), hex(), oct(), tuple(), set(), list(), dict(), etc. for the type casting in python.

There are two varieties of typecasting in python:
    1. Explicit Conversion(Explicit type casting in python) 
    2. Implicit Conversion(Implicit type casting in python)

The conversion of one data type into another, done via user intervention or manually as per the requirement, is known as explicit type conversion. 
On the other hand, in Implicit type conversion, Python automatically converts one data type to another data type without any user's need.

'''
