#Find the sum of three-digit number. 

num=int(input("Enter a three-digit number: "))

hundred= num//100
ten=(num//10)%10
one=(num%10)

sum=hundred+ten+one

print("Sum of digits:", sum)