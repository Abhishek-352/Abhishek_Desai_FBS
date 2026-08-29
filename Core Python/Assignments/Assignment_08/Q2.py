# Write a program to calculate area of circle

def area_circle(r):
    area=3.14*r*r
    return area
r=int(input("Enter your radius: "))

res=area_circle(r)

print("Area of circle: ",res)