#  WAP to check if a given number is prime number or not. 

n = int(input("Enter a number: "))

i = 2
count = 0

while i < n:
    if (n % i == 0):
        count = count + 1
    i = i + 1

if (n > 1) and (count == 0):
    print("Prime Number")
else:
    print("Not a Prime Number")