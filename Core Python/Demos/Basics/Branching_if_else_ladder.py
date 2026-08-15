# if else ladder

#check number is positive, negative or neutral

num=int(input("Enter your number: "))
if(num==0):
    print("Give number is Neutral: ",num)
elif(num>0):
    print("Number is Positive: ",num)
elif(num<0):
    print("Nuber is Negetive: ",num)
else:
    print("Enter valid input.")


#check number range between 1 to 250

num=int(input("Enter your number: "))
if (num<=0):
    print("Number is less than zero or Number is zero: ",num)
elif(num<=50):
    print("range is between 1 to 50: ",num)
elif(num<=100):
    print("range is between 51 to 100: ",num)
elif(num<=150):
    print("range is between 101 to 150: ",num)
elif(num<=250):
    print("range is between 151 to 250: ",num)
