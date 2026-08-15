# Write a program to input angles of a triangle and check whether triangle is valid or not. 

a1=int(input("Enter your 1 angle: "))
a2=int(input("Enter your 2 angle: "))
a3=int(input("Enter your 3 angle: "))

sum=a1+a2+a3
if(sum==180) and (a1 > 0 and a2 > 0 and a3 > 0):
    print("Triangle is valid.")
else:
    print("Triangle is not Vaild.") 