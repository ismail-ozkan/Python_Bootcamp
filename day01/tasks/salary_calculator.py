name = input("Enter your name:")
hourly_rate = float(input("Enter your hourly rate:"))
weekly_hour = int(input("How many hours you work in a week?"))

salary = 52 * hourly_rate * weekly_hour

print(f"Hello {name}, your salary is $ {salary}")