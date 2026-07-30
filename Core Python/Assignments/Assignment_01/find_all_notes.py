amount = int(input("Enter the total amount: "))

note500 = amount // 500
amount = amount % 500

print("\n""500 Notes =", note500)
print("Remaining Amount =", amount)

note200 = amount // 200
amount = amount % 200

print("\n""200 Notes =", note200)
print("Remaining Amount =", amount)

note100 = amount // 100
amount = amount % 100

print("\n""100 Notes =", note100)
print("Remaining Amount =", amount)

note50 = amount // 50
amount = amount % 50

print("\n""50 Notes =", note50)
print("Remaining Amount =", amount)

note20 = amount // 20
amount = amount % 20

print("\n""20 Notes =", note20)
print("Remaining Amount =", amount)

note10 = amount // 10
amount = amount % 10

print("\n""10 Notes =", note10)
print("Remaining Amount =", amount)