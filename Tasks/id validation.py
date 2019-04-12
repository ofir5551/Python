id = input("Enter id: ")

if len(id) < 9:
    id = '0'* (9-len(id)) + id               # Task 1

id2 = '121212121'                         # Task 2

id3 = [0,0,0,0,0,0,0,0,0]

for x in range(0, len(id3)):
    id3[x] = int(id[x]) * int(id2[x])       # Task 3
    
id4 = [0,0,0,0,0,0,0,0,0]
for x in range(0, len(id3)):                # Task 4
    if id3[x] > 9:
        id4[x] = id3[x]%10 + id3[x]//10
    else:
        id4[x] = id3[x]

sum = 0

for x in range(0, len(id4)): 
    sum+=id4[x]

print(id)
print(id2)
print(id3)
print(id4)

if sum % 10 == 0:                           # Task 5
    print("Good ID")
else:
    print("Bad ID")