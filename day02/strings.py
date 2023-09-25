name = 'Python'
#       012345

length = len(name)

print(length)

print(name[1])  # 2. character in the name is 'y'

# print last character

print(name[len(name) - 1])  # n
print(name[-1])  # n

# Slicing String
# using both starting and ending indexes
s = 'Java Programming Language'

print(s[5:16])  # Programming
print(len(s[5:16]))  # 11

# using just ending index
print(s[:4])  # Java

# using just staring index

print(s[17:])  # Language

# reversing string
print(s[::-1])

s1 = 'Python Programming'

s2 = str(reversed(s1))

print(type(s2))
reversed(s2)

print(s2)  # <reversed object at 0x00000243935DBFD0>

s7 = 'CYDEO SCHOOL'

print("------------------------")

# print(help(str))
print("-----------------------------")

s8 = "python programming language"

s8 = s8.capitalize()
print(s8)

s8 = s8.title()
print(s8)

print("----------")
# strip methods
s9 = "  cydeo  "

s10 = s9.split()
s11 = s.lstrip()
s12 = s.rstrip()

print(s10)
print(s11)
print(s12)

print("---------")

# index rindex

st = "JAVA"
print(st.index('A'))
print(st.rindex('A'))

st = "Java Java"

st = st.replace("Java", 'Python')
print(st)

st = st.replace("Python", 'C#', 1)
print(st)

s = 'JAva JaVA JAvA jaVa Python'


count_java = s.lower().count('java') #find and count as a substring
count_python = s.count('Python')

print(count_java)
print(count_python)


s1 = 'java'
s2 = 'JAVA'

print(s1 == s2)

print(s1.lower() == s2.lower()) #ignore case, it's onyl way to do this


s = 'Java'

print(s.islower())
print(s[0].islower())
print(s[-1].islower())
print(s[-4].isupper()) #True


s = 'a'

print(s.isdigit())
print(s.isalpha())

s = 'It Is Title'

print(s.istitle())
