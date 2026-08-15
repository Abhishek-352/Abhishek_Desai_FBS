# Input 5 subject marks from user and display grade(eg.First class,Second class ..) 

sub1=int(input("Enter your marks out of 100: "))
sub2=int(input("Enter your marks out of 100: "))
sub3=int(input("Enter your marks out of 100: "))
sub4=int(input("Enter your marks out of 100: "))
sub5=int(input("Enter your marks out of 100: "))

average=float(sub1+sub2+sub3+sub4+sub5)/500
percentage=float(average*100)

if(percentage>=80)and(percentage<=100):
    print("A Grade.")
elif(percentage>=60)and(percentage<80):
    print("B Grade")
elif(percentage>=35)and(percentage<=60):
    print("C Grade")
else:
    print("Falid")
    
