# addition of previous two values change third value 

n=int(input("Enter your number: "))
a= -1
b= 1

for i in range(1,n+1):
    c=a+b
    print(c,end=' ')
    a=b
    b=c
