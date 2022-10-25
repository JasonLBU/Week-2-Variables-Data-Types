# Task 1 - Completed
name = input("Hello, what is your name? ")
print("Hello, " + name + ". Good to meet you!")
print()

# Task 2 Celsius to Fahrenheit - Completed
celsius = float(input("Enter a temperature in celsius: "))
fahrenheit = float((celsius * 1.8) + 32)
print(str(celsius) + "C is equivalent to " + str(fahrenheit) + "F")
print()

# Task 3 - Student Groups - Completed
StudentNum = int(input("How many students are there in total? "))
GroupSize = int(input("What will the group size be? "))
GroupNum = StudentNum // GroupSize
LeftOver = StudentNum % GroupSize

# Task 3 Extension: - Completed
if LeftOver % 10 == 0:
    print("There will be " + str(GroupNum) + " groups with " + str(LeftOver) + " students left over")
else:
    print("There will be " + str(GroupNum) + " groups with " + str(LeftOver) + " student left over")
print()

# Task 4 - Completed
SweetsNum = int(input("How many sweets are there? "))
TotalPupils = int(input("How many pupils do you have? "))
EqualAmount = SweetsNum // TotalPupils
SweetsLeft = SweetsNum % TotalPupils

print("Each pupil will have " + str(EqualAmount) + " sweets and you'll have " + str(SweetsLeft) + " left over sweets")
print()
