# 4. Calculate the cost of painting the following building’s walls (both interior and 
# exterior). You need to accept area (one wall) and cost of both interior and 
# exterior wall.  
# (Note: 1. Below diagram is of two joint rooms. 
# 2. It is upper view of building.) 

area = float(input("Enter area of one wall: "))

in_cost = float(input("Enter interior painting cost: "))
ex_cost = float(input("Enter exterior painting cost: "))

in_total = area * in_cost
ex_total = area * ex_cost

total_cost = in_total + ex_total

print("Interior painting cost =", in_total)
print("Exterior painting cost =", ex_total)
print("Total painting cost =", total_cost)