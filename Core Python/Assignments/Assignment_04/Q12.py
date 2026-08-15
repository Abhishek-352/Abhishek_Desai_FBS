# Write a program to check if given number is Armstrong number or not.  
# (Hint : 153 = 1*1*1 + 5*5*5 + 3*3*3 , 1634 = 1*1*1*1 + 6*6*6*6 + 3*3*3*3 +  
# 4*4*4*4)

n = int(input("Enter a number: "))

temp = n
digits = 0

# Count number of digits
while temp > 0:
    digits = digits + 1
    temp = temp // 10

temp = n
sum = 0

# Calculate Armstrong sum
while temp > 0:
    digit = temp % 10
    sum = sum + digit ** digits
    temp = temp // 10

if sum == n:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")