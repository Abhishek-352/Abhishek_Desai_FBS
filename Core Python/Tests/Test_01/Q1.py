#  Write a program to find the area and perimeter of following figure (Accept the 
# length, breadth and radius from user:
#  
print("For Rectangle")

l=int(input("Enter Length: "))
b=int(input("Enter breadth: "))

area=l*b
perimeter= 2 * (l + b)

print("Area of a Rectangle: ",area)
print("perimeter of a Rectangle:",perimeter)



print("For Square")

side = int(input("Enter side: "))

area = side * side
perimeter = 4 * side

print("Area =", area)
print("Perimeter =", perimeter)


print("For Circle")

radius = float(input("Enter radius: "))

area = 3.14 * radius * radius
perimeter = 2 * 3.14 * radius

print("Area =", area)
print("Perimeter =", perimeter)



