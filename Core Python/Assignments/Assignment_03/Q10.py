# #  Write a program to check if person is eligible to marry or not (male age >=21 and 
# female age>=18)

gender=input("Enter your Gender(M/F): ")
age=int(input("Enter your Age: "))

if(gender=='f') or (gender=='F'):
    if(age>=18):
        print("Women is Eligible to Marry")
    else:
        print("Women is not Eligible to Marry")
else:
    if(gender=='m') or (gender=='M'):
        if(age>=21):
            print("Men is Eligible to Marry")
        else:
            print("Men is not Eligible to Marry")
    else:
        print("Enter Valid Gender.")
