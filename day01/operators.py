# aritmetic : +, -, *, /, %

print(10 + 2)
print(10 - 2)

print(10 * 3)

print(10 / 3)
print(10 / 2) # it returns always float value

print(10 % 3)

print(int(100/2)) #50


# shorthand assignment operators : = , +=, -=, /= and *=

a = 100

a -= 50
print(a)

a *= 2

print(a)

#print('\n\033[31m')???
print('\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')
print('\t\t\t*                                                                               *')
print('\t\t\t*                                                                               *')
print('\t\t\t*                           Time is up!                                         *')
print('\t\t\t*                                                                               *')
print('\t\t\t*                                                                               *')
print('\t\t\t* * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * *')


# logical operators: and, or, not

s = 'Hello World'

print('H' and 'W' in s)

print(True and True)
print(True and False)
print(True or False)
print(not True or False)

s = 'Java Python C#'

print('Java' or 'Ruby' in s) # it returns Java


age = 29
citizen_ship = 'USA'
is_eligible = age >= 18 and citizen_ship == 'USA'

print(is_eligible)

has_java = 'Java' in s

# !contains()
print('Python' not in s)

print(not False)
print(not True) # ! like Java

print("---------------------------")

s = 'Java'
s2 = 'Java'
s3 = 'Ja' + 'va'
s4 = 'va'
s5 = 'Ja{}'.format(s4)
print(s5)
print(s is s2)
print(s is s3) # True
print(s is s5) # False -> Check memory address
print(s == s5) # Ture -> Check context of object



# ==  ->  context of object
# 'is' keyword ->   reference(memory address) of object