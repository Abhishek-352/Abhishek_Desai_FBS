#  Write a program to calculate area of rectangle 

def area_rectangle(length, breadth):
    area = length * breadth
    return area


length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

result = area_rectangle(length, breadth)

print("Area of rectangle =", result)