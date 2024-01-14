# 9 prime number or composite number

num = int(input("Enter any number : "))

if num == 1:
    print("1 is neither prime nor composite")
    exit()

if num == 2:
    print("prime")
    exit()

# loop to see whether prime or composite
prime = True

for i in range(2, num):
    if num % i == 0:
        prime = False
        break

if prime == True:
    print("prime")
else:
    print("composite")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 10. prime numbers between 2 to 100

count = 0

for i in range(2, 101):
    prime = True
    if i == 2:
        print(i)
        count += 1
        continue

    for j in range(2, i):
        if i % j == 0:
            prime = False
            break

    if prime == True:
        print(i)
        count += 1

print("total prime numbers between 2 to 100 are", count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 11. composite numbers between 2 to 100

count = 0

for i in range(2, 101):
    composite = False
    if i == 2:
        continue

    for j in range(2, i):
        if i % j == 0:
            composite = True
            break

    if composite == True:
        print(i)
        count += 1

print("Total no. of composite numbers between 2 to 100 is", count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 12. Reverse a given string

normalString = str(input("Enter any string : "))

length = len(normalString)

reversedString = ""

i = 0

while i < length:
    reversedString = normalString[i] + reversedString
    i += 1

print("reverse :", reversedString)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 13. count the number of occurences of given character in a given string

normalString = "Santosh Bhaykatte"
char = 't'

i = 0
count = 0

while i < len(normalString):
    if normalString[i] == char:
        count = count + 1
    i += 1

print("Number of occurence is", count)

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++

# 14. string palindrome

normalString = str(input("Enter any string : "))
tempString = normalString

length = len(normalString)

reversedString = ""

i = 0

while i < length:
    reversedString = normalString[i] + reversedString
    i += 1

if tempString == reversedString:
    print("palindrome")
else:
    print("not palindrome")

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++
    

    
