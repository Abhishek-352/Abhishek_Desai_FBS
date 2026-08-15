# Write a program to enter P, T, R and calculate Compound Interest. 

p=int(input("Enter principle amout: "))
r=float(input("Enter rate of intrest: "))
t=int(input("Enter time(year): "))

a=p *(1+ r/100)
ci=a-p

print(f"compound intrest on your principle amount is {ci}")