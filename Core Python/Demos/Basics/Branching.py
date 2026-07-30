##Branching:

##1.if

# num1=int(input("Enter your number: "))

# if (num1>0):
#     print("Number is positive: ",num1)


##2.if else
# num1=int(input("Enter your number: "))

# if (num1%2==0):
#     print("\n""Number is even: ",num1)
# else:
#     print("\n""Number is odd: ",num1)


# ##3.Nested if else

# gender=input(("Enter yor gender(M/F): "))
# age=int(input("Enter your age: "))

# if(gender=='F'):

#     if(age>=18):
#         print("Girls is Eligible for Marriage.")
#     else:
#         print("Girls is not Eligible for Marriage. ")
# else:

#     if(age>=21):
#         print("Boy is Eligible for Marriage.")
#     else:
#         print("Boy is not Eligible for Marriage.")


##4.if else ladder

# num=int(input("Enter your number: "))

# if(num==0):
#     print("Give number is Neutral: ",num)
# elif(num>0):
#     print("Number is Positive: ",num)
# elif(num<0):
#     print("Nuber is Negetive: ",num)
# else:
#     print("Enter valid input.")


# num=int(input("Enter your number: "))

# if (num<=0):
#     print("Number is less than zero or Number is zero: ",num)
# elif(num<=50):
#     print("range is between 1 to 50: ",num)
# elif(num<=100):
#     print("range is between 51 to 100: ",num)
# elif(num<=150):
#     print("range is between 101 to 150: ",num)
# elif(num<=250):
#     print("range is between 151 to 250: ",num)

num=int(input("Enter your number: "))

if (num<=0):
    print("Number is less than zero or Number is zero: ",num)   
    if(num<=50):
         print("range is between 1 to 50: ",num)
    else:
        if (num<=100):
            print("range is between 51 to 100: ",num)
        else:
            if(num<=150):
                print("range is between 101 to 150: ",num)

            
            
