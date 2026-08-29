#  Write a program to find sum of following series using functions : 
# a.  1+ 2 + 3 + 4+….. + n 
# b. 1!+ 2! + 3! + 4!+….. + n! 
# c. 1^1 + 2^2 + 3^3+ …… n^n 


print(" a.  1+ 2 + 3 + 4+….. + n ")
def sum_series(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i

    return total

n = int(input("Enter n: "))

result = sum_series(n)

print("Sum =", result)



print('\n''b. 1!+ 2! + 3! + 4!+….. + n! ')
def factorial_sum(n):
    total = 0
    fact = 1

    for i in range(1, n + 1):
        fact = fact * i
        total = total + fact

    return total

n = int(input("Enter n: "))

result = factorial_sum(n)

print("Sum of factorial series =", result)



print('\n''c. 1^1 + 2^2 + 3^3+ …… n^n')
def power_sum(n):
    total = 0

    for i in range(1, n + 1):
        total = total + i ** i

    return total


n = int(input("Enter n: "))

result = power_sum(n)

print("Sum =", result)