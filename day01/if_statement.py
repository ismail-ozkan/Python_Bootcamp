if False:
    print("Smile")

print("this block is out of if statements")

# False usage
# if True:
# print("Smile") -> we need to use "INDENTATION" -> at least one space but using paragraph space is better to read

score = 80
if score >= 60:
    print('Congrats! You have passed the exam!')
    # if block cannot be empty

if score <= 59:
    pass  #

s = 'Hello World'

if 'H' and 'W' in s:
    print(s, 'has', 'H', 'and', 'W')

print('---------------------------')

if score >= 60:
    print('Pass')
else:
    print('Fail')

print('---------------------------')

age = 20
result = None

if age >= 21:
    result = 'Eligible'
else:
    result = 'Not eligible'

print(result)

print('---------------------------')
# Ternary Example
age = 26
result = 'Eligible' if age >= 21 else 'Not eligible'

print(result)

print('---------------------------')

num = -3
res = None
if num > 0:
    res = 'Positive'
elif num < 0:
    res = 'Negative'
else:
    res = 'Zero'

print(res)

# Ternary with elif is not exist
# #
# # num2 = 40
# is_old = True num2>40 if elif num2<40 False

print('-----------------------------')

score = -300

if 100 >= score >= 0:
    if score >= 60:
        print('PASS')
    else:
        print('FAIL')
else:
    print('Score is not valid')

print("--------------------------------")

score = 70

if 100 >= score >= 0:
    if score < 40:
        print('F')
    elif 40 <= score <= 60:
        print('D')
    elif 60 <= score <= 80:
        print('C')
    elif 80 <= score <= 90:
        print('B')
    elif 90 <= score:
        print('A')
else:
    print('Invalid Score')

