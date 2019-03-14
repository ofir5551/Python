num = int(input("Enter number"))

if num<10 and num>0:
    if num == 1:
        print("one")
    if num == 2:
        print("two")
    if num == 3:
        print("three")
    if num == 4:
        print("four")
    if num == 5:
        print("five")
    if num == 6:
        print("six")
    if num == 7:
        print("seven")
    if num == 8:
        print("eight")
    if num == 9:
        print("nine")
if num > 9 and num < 100:
    print("this number has 2 digits and the sum is:", (num//10)+(num%10))
if num > 99 and num < 1000:
    print("this number has 3 digits and the sum is:", (num//100) * ((num//10) % 10) * (num%10)) 

elif num < 0:
    print("This number is negative")
else:
    print("This number has more than 3 digits")