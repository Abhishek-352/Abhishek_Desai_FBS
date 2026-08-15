# Write a program to check if user has entered correct userid and password.

id=input("Enter your ID:")
password=input("Enter your password: ")

if(id=='admin')and(password=="12345"):
    print("Login Successful")
else:
    print("Login Faild")