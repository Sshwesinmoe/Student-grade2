name = input("Enter student name: ")
mark1 = float(input("Enter first subject mark: "))
mark2 = float(input("Enter second subject mark: "))

total = mark1 + mark2
average = total/ 2

print(f"Student Name: {name}")
print(f"Total Mark: {int(total)}")
print(f"Average Mark: {average:.0f}")
