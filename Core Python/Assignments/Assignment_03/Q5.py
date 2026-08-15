# Write a program to check whether the triangle is equilateral, isosceles or scalene 
# triangle.

a=int(input("Enter your first side: "))
b=int(input("Enter your second side: "))
c=int(input("Enter your third side: "))

if(a==b==c):
    print("Triangle is Equilateral.")
elif(a==b)or(b==c)or(a==c):
    print("Triangle is isosceles.")
elif(a!=b)and(b!=c)and(c!=a):
    print("Triangle is scalene.")
    