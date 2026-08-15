#  Write a program to check if given 3 digit number is a palindrome or not.

num=int(input("Enter your three-digit number: "))

first=num//100
last=num%10

if(first==last):
    print("Your three-digit number is palindrome")
else:
    print("Your three-digit number is not palindrome")