
for i in range(1, 6):
    print(i)
    if i == 3:
        break

print("---------------------")

for i in range(1, 6):
    if i == 3 or i == 4:
        continue
    print(i)

print("---------------------")

for i in range(1, 6):
    if i == 3 or i == 4:
        pass
    print(i)

if True:
    pass

class Class:

    def method(self):
        pass

    pass
