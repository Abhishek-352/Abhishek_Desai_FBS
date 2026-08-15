# 2. Write a program to calculate simple interest based on Principal, Rate and Time 
# (SI = P*R*T/100)  


p=int(input("Enter principle amout: "))
r=float(input("Enter rate of intrest: "))
t=int(input("Enter time(year): "))

si=(p *r *t)/100

print(f"Simple intrest on your principle amount is {si}")