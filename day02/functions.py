"""

Java Methods
    public static void method(parameters) {

    }

"""
import numbers


def display_message():
    print('Hello Cydeo')
    print('Hello World')


display_message()


def value():
    return 5


print(value())

s = value()

print(s)


def return_int() -> int:  # Return type is mandatory, arrow expression is used for determing type of function
    return 10


print(return_int())


def display_value(value):
    print(value)


display_value('ismail')


def square(number):
    return number * number


def square(num: int):  # while writing : int after num parameter we just say int is preferred option to use in function
    return num * num


print(square(3))


# print(square('Hello'))


def divide(num1, num2):
    return num1 / num2


print(divide(100, 20))


def add(num1: int, num2: int) -> int:
    return num1 + num2


def add(num1: numbers, num2: numbers) -> numbers:
    return num1 + num2


print(add(100, 20))
print(add(10.3, 20.3))

print('----------------------------------')


def calculate(num1: numbers, num2: numbers, operator: str) -> numbers:
    if operator == '-':
        return num1 - num2
    elif operator == '+':
        return num1 + num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        print('Invalid operator')
        return 0


print(calculate(10, 3, '-'))

print("------------------------")


# method overloading

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    # we can provide default values for parameters which are we don't need to use.
    # This is how we implement method overloading in Python
    # There is no default values for parameters and data types in Python
    return n1 + n2 + n3 + n4


print(sum(1, 5))
print(sum(3, 6, 8))


def multiply(n1: numbers, n2: numbers, n3: numbers = 1, n4: numbers = 1):
    return n1 * n2 * n3 * n4


class test:
    def method(self):  # when we create a function in class we call it "Method"
        pass


print('--------------------------------')


def concat(a: str, b, c='', d='', e=''):  # last three arguments are optional
    print(f'{a} {b} {c} {d} {e}'.strip())


concat('Cydeo', 'School')

concat('Pyhton', 'is', 'my', 2, 'language')
concat('Pi', 'is', 3.11, '->' ,False)

"""
1. Declaring
2. Parameters
3. Restricting parameter' data types
4. Setting default value to parameter
5. Restricting return type (using -> arrow )

Dynamic Typing -> varible = data  # so we don't need to specify dataType like Java

"""