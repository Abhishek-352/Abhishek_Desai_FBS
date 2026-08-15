#  WAP to print sum of series upto n.  

n = int(input("Enter n: "))

i = 0
sum = 0

while i <= n:
    sum = sum + i
    i = i + 1

print("Sum =", sum)