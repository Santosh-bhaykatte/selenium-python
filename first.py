# Written by - Santosh Bhaykatte

# for loop -

# Syntax => for var-name in variable/ds-name:

'''
d = [0, 1, 2, 3, 4, 5, "santosh"]

for var in d:
    print(var)

print("No more elements in d")
'''
import math

'''
game = ["cricket", "football", "golf", "badminton"]
# game[1] = "tennis" # allowed because list is mutable

print(game)

# ++++++++++++++++++++++++++++++++
for var in game:
    print(var)

print("No more elements in \'game\' list")
'''
# ++++++++++++++++++++++++++++++++

'''
for var in "Santosh":
    print(var)
'''
# ++++++++++++++++++++++++++++++++

'''
for i in range(1, 11):
    print(i)
'''
# ++++++++++++++++++++++++++++++++

'''
for var in range(1, 31):
    if var % 3 == 0:
        print(var)
'''

# ++++++++++++++++++++++++++++++++

# table of number
'''
num = int(input("Enter any number : "))

for i in range(1, 11):
    table = num * i
    print(table)
'''

# ++++++++++++++++++++++++++++++++

# nested for loop

'''
a1 = ["C lang", "C++ lang"]
b1 = ["POP", "OOP"]

for i in range(1, 3):
    for j in range(1, 3):
        print(i, j)
'''
# ++++++++++++++++++++++++++++++++

'''
1
12
123
1234
12345
'''

# code
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end="")
    print()
'''

# ++++++++++++++++++++++++++++++++

'''
1
22
333
4444
55555
'''
# code
'''
for i in range(1, 6):
    for j in range(1, i+1):
        print(i, end="")
    print()
'''
# ++++++++++++++++++++++++++++++++

'''
12345
1234
123
12
1
'''

# code
'''
k = 6
for i in range(1, 6):
    for j in range(1, k):
        print(j, end="")
    k = k - 1
    print()
'''

# ++++++++++++++++++++++++++++++++

'''
55555
4444
333
22
1
'''
# code

'''
k = 5
m = 6
for i in range(1, 6):
    for j in range(1, m):
        print(k, end="")
    k = k - 1
    m = m - 1
    print()
'''

# ++++++++++++++++++++++++++++++++

'''
54321
5432
543
54
5
'''
# code
'''
for i in range(1, 6):
    for j in range(5, i-1, -1): # here, -1 meant for reverse count like 54321
        print(j, end="")
    print()
'''

# ++++++++++++++++++++++++++++++++

'''
5
54
543
5432
54321
'''
# code
'''
k = 4
for i in range(1, 6):
    for j in range(5, k, -1):
        print(j, end="")
    k = k - 1
    print()
'''

# ++++++++++++++++++++++++++++++++

'''
5
44
333
2222
11111
'''
# code
'''
k = 5
for i in range(1, 6):
    for j in range(6, k, -1):
        print(k, end="")
    k = k - 1
    print()
'''

# ++++++++++++++++++++++++++++++++

# LOGICAL PROGRAMS

# 1. Factorial of number - factorial of 4 = 1x2x3x4

'''
num = int(input("Enter any number : "))

fact = 1

for i in range(1, num + 1):
    fact = fact * i

print("Factorial of", num,"is", fact )
'''

# ++++++++++++++++++++++++++++++++

# 2. even or odd
'''
num = int(input("Enter any number : "))

if num % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

# ++++++++++++++++++++++++++++++++

# 3. positive or negative

'''
num = int(input("Enter a number : "))

if num >= 0:
    print("Positive")
else:
    print("negative")
'''

# ++++++++++++++++++++++++++++++++

# 4. reverse a number

'''
num = int(input("Enter a number : "))
temp = num
rev = 0

while num != 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

print("Reverse of", temp,"is", rev)
'''

# ++++++++++++++++++++++++++++++++

# 5. palindrome

'''
num = int(input("Enter a number : "))
temp = num
rev = 0

while num != 0:
    digit = num % 10
    rev = rev*10 + digit
    num = num // 10

if rev == temp:
    print("palindrome")
else:
    print("not palindrome")
'''

# ++++++++++++++++++++++++++++++++

# 6. armstrong number

'''

num = int(input("Enter any number : "))

temp = num
cubeSum = 0
len = 0

# calculating number of digits in number

while temp != 0:
    temp = temp // 10
    len = len + 1

print("number of digits :", len)

temp = num

while num != 0:
    digit = num % 10
    cubeSum = cubeSum + (digit ** len)
    num = num // 10

if cubeSum == temp:
    print("Armstrong")
else:
    print("Not Armstrong")
    
'''

# ++++++++++++++++++++++++++++++++

# 7. armstrong numbers between 1 to 10000

'''
for i in range(1, 10000):
    temp = i
    cubeSum = 0
    len = 0

    while temp != 0:
        temp = temp // 10
        len = len + 1

    temp = i

    while i != 0:
        digit = i % 10
        cubeSum = cubeSum + (digit ** len)
        i = i // 10

    if cubeSum == temp:
        print(temp)

'''

# ++++++++++++++++++++++++++++++++

# 8. fibonacci series - 0, 1, 1, 2, 3, 5, 8, 13, 21

'''
num = int(input("Enter a limit : ")) # limit - no. values to print excluding starting 0 & 1

n1 = 0
n2 = 1

print(n1,",",n2, end="")

for i in range(1, num + 1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    print(" ,",n3, end="")

'''

# ++++++++++++++++++++++++++++++++

# 9 prime number or composite number

'''
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
'''

# ++++++++++++++++++++++++++++++++

# 10. prime numbers between 2 to 100

'''
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
'''

# ++++++++++++++++++++++++++++++++

# 11. composite numbers between 2 to 100

'''
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
'''

# ++++++++++++++++++++++++++++++++

# 12. Reverse a given string

'''
normalString = str(input("Enter any string : "))

length = len(normalString)

reversedString = ""

i = 0

while i < length:
    reversedString = normalString[i] + reversedString
    i += 1

print("reverse :", reversedString)

'''

# ++++++++++++++++++++++++++++++++

# 13. count the number of occurences of given character in a given string

'''
normalString = "Santosh Bhaykatte"
char = 't'

i = 0
count = 0

while i < len(normalString):
    if normalString[i] == char:
        count = count + 1
    i += 1

print("Number of occurence is", count)

'''

# ++++++++++++++++++++++++++++++++

# 14. string palindrome

'''
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
'''

# ++++++++++++++++++++++++++++++++