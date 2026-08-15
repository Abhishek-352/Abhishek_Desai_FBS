# # Write a program to input all sides of a triangle and check whether triangle is valid or 
# not. 

a=int(input("Enter your first side: "))
b=int(input("Enter your second side: "))
c=int(input("Enter your third side: "))

if(a+b>c)and(a+c>b)and(b+c>a):
    print("Triangle is valid.")
else:
    print("Triangle is not valid.")
    