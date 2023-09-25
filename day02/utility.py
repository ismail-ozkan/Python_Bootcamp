import numbers

print('This is utility module')
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

def sum(n1: numbers, n2: numbers, n3: numbers = 0, n4: numbers = 0) -> numbers:
    # we can provide default values for parameters which are we don't need to use.
    # This is how we implement method overloading in Python
    # There is no default values for parameters and data types in Python
    return n1 + n2 + n3 + n4

def concat(a: str, b, c='', d='', e=''):  # last three arguments are optional
    print(f'{a} {b} {c} {d} {e}'.strip())

