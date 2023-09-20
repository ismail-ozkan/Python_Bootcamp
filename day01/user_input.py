#print(  help(input))
# We can you help method before using any method


name = input('Enter your name:\n')
age = int(input('Enter your age:\n'))
gpa = float(input('Enter your gpa:\n'))
boolean_value = bool(input('Enter True or False:\n'))

print(type(age)) #int
print(type(gpa)) #float
print(type(boolean_value)) #bool

# age +=5 error

#age = int(age) + 5 we can specify this condition while using input method

age +=5  # not error
print('Your name is {} and your age is {}'.format(name, age))
print(boolean_value)

