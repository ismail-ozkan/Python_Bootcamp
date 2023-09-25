
s = 'Python'

for each in s:
    print(each)

print("---")
for i in range(0,len(s)):
    print(s[i])

print("-----")

for i in range(-len(s),0):
    print(s[i])

print('----------------')

for i in reversed(range(0,len(s))):
    print(s[i])

print('----------------')
print("reversed(s)")
for x in reversed(s):
    print(x)

print('----------------')
print("s[::-1]")
for x in s[::-1]:
    print(x)

print('----------------')

result = ''

for x in s[::-1]:
    result += x

print("result : "+result)

print('----------------')

#for i in range(10):
for i in range(1, 11):
    print(f'{i}) Hello')

print('----------------')

num = int(input("Enter a positive number:\n"))

while num<=0:
    num = int(input("Enter a positive number:\n"))

print(f'You have entered {num}')

print("--------------------------------")

anwser = input('Enter yes or no:\n')

while not (anwser.lower() == 'yes' or anwser.lower() == 'no'):
    anwser = input('Enter yes or no:\n')

print(f'You have entered {anwser}')

# Branching statements
