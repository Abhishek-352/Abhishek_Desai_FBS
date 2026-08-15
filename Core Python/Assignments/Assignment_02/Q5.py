# WAP to calculate selling price of book based on cost price and discount. 

cost_price = float(input("Enter the cost price of the book: "))
discount = float(input("Enter the discount percentage: "))

selling_price = cost_price - (cost_price * discount / 100)

print("Selling price of the book: ", selling_price)
