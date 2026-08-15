# Write a program to enter P, T, R and calculate simple Interest. 

p=int(input("Enter principle amout: "))
r=float(input("Enter rate of intrest: "))
t=int(input("Enter time(year): "))

si=(p *r *t)/100

print(f"Simple intrest on your principle amount is {si}")