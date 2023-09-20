"""
In Java: static Typing
    DataType variableName = Data;

-- Python is slower than Java

In Python: Dynamic Typing
    variable_name = data

"""
# Built-in data types in Python
"""
Python - Data Types
    1 Numeric
        - Integer
        - Float
        - Complex Number
    2 Boolean
    3 Set
    4 Dictionary 
    5 Sequence
        - List
        - Tuple
        - String
"""
name = None # like null in Java
print(name)
name = 'ismail'
print(name)
# type() function is used for learning data type
print(type(name))

age = 32

print(type(age))

pi = 3.141
print(type(pi))
# Python is also OOP language

is_married = True

print(type(is_married)) # bool

# type casting

a = 5
# I need to convert it 5.0
b = float(a)

print(b)

x = "19.99"

y = float(x)

print(y + b) #24.99

z = "10.999"
t = int(float(z))
print(a+t) # 15

n1 = 3
n2 = 2
n3 = n1+n2
s1 = str(n3)

print(s1 + " : 5")


n1 = 32

n1 = str(n1)

print("num :" + n1)
