# Write a program to swap two numbers without using third variable.

a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print('\n'"Before swapping: a =", a, "b =", b)

a = a + b
b = a - b
a = a - b

print('\n'"After swapping: a =", a, "b =", b)