sub1=int(input("Enter your Mathematic marks out of 100: "))
sub2=int(input("Enter your English marks out of 100: "))
sub3=int(input("Enter your Science marks out of 100: "))
sub4=int(input("Enter your Gerography marks out of 100: "))
sub5=int(input("Enter your History marks out of 100: "))

average=float(sub1+sub2+sub3+sub4+sub5)/500
percentage=float(average*100)

print("Percentage of student in 5 subjects: ",percentage)
