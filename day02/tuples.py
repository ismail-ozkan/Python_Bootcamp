days_1 = ('Monday')
print(type(days_1))  # str

days_2 = ('Monday',)
print(type(days_2))  # tuple

days = ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')

print(len(days))  # 7

print(days)

# work_days = days[0:5]
# work_days = days[:5]
work_days = days[0:-2]

print(work_days)

# weekends = days[5:]
weekends = days[-2:]

print(weekends)
# tuple merging
new_days = work_days + weekends

print(f'new_days: {new_days}')

#     ==        ,         is
# checking context     checking memory address( == operator in Java)

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 3)

print(tuple1 == tuple2)
print(tuple1 is tuple2)

tuple3 = tuple1 + tuple2

print(tuple3)

print(tuple3.count(3))  #2

tuple4 = tuple1 * 5
print(tuple4)

reversed_days = days[::-1]

print(reversed_days)

print(reversed_days.index('Saturday')) # 1
print(days.index('Saturday')) # 5

numbers = 10, 10, 10, 10, 20, 30, 10, 50, 10, 10

print(numbers.count(10))

print("--------------------------")

for x in days:
    print(f'{days.index(x)+1}) {x}')

print("--------------------------")

for i in range(0, len(days)):
    print(f'{i+1}) {days[i]}')


