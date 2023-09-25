from utility import sum, calculate

result = calculate(10,20, '*') # if we import some methods from a module not all module, we call them just with their names

print(result)

import utility

utility.concat('test', 2)
utility.sum(1,3)
utility.calculate(33, 3 , '*')

print('-----------------------------------')

import utility as u

u.concat('test', 2)
u.sum(1,3)
u.calculate(33, 3 , '*')

print('-----------------------------------')

from utility import sum as s, calculate as c

total = s(33,3,4,66)
# s refers to sum
print(total)

# from keyword for using partial import