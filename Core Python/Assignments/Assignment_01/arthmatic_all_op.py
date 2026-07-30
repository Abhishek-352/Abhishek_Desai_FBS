#input take always string value we have to mention our type

num1=int(input("Enter number 1: "))
num2=int(input("Enter number 2: "))

sum=num1+num2
print('\n'f"Addition of {num1} and {num2} is {sum}.")
print("Addition:",sum,"\n")

sub=num1-num2
print(f"Subtraction of {num1} and {num2} is {sub}.")
print("Subtraction:",sub,"\n")

mul=num1*num2
print(f"Multiplication of {num1} and {num2} is {mul}.")
print("Multiplication:",mul,"\n")

div=num1/num2
print(f"Division of {num1} and {num2} is {div}.")
print("Division:",div,"\n")

floor_div=num1//num2
print(f"Floor Division of {num1} and {num2} is {floor_div}.")
print("Floor Division:",floor_div,"\n")

mod=num1%num2
print(f"Modulus of {num1} and {num2} is {mod}.")
print("Modulus:",mod,"\n")

exp=num1**num2
print(f"Exponentiation of {num1} and {num2} is {exp}.")
print("Exponentiation:",exp,"\n")
