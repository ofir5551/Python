age = int(input("Enter your age"))

if age < 0:
    print("Invalid age")
elif age < 18:
    print("Too young")
    print("You can buy a soft drink")
else:
    print("Too old")
    print("You can buy wine")

print("Your age is", age)
