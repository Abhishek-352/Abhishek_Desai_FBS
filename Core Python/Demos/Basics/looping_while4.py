#WAP to separate the digits using while loop

num=int(input("Enter a number: "))

while(num>0):
    digit=num%10
    print(digit)
    num=num//10

print("All digits are separated")