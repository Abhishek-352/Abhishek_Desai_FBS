# Nested if else

## checking eligibility for marriage

gender=input(("Enter your gender(M/F): "))
age=int(input("Enter your age: "))
if(gender=='F'):
    if(age>=18):
        print("Girls is Eligible for Marriage.")
    else:
        print("Girls is not Eligible for Marriage. ")
else:
    if(age>=21):
        print("Boy is Eligible for Marriage.")
    else:
        print("Boy is not Eligible for Marriage.")


#check number range between 1 to 250

num=int(input("Enter your number: "))
if (num<=0):
    print("Number is less than zero or Number is zero: ",num)
else:
    if(num<=50):
        print("range is between 1 to 50: ",num)
    else:
        if(num<=100):
            print("range is between 51 to 100: ",num)
        else:
            if(num<=150):
                print("range is between 101 to 150: ",num)
            else:
                if(num<=250):
                    print("range is between 151 to 250: ",num)