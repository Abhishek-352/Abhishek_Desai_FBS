# Accept age of five people and also per person ticket amount and then calculate total 
# amount to ticket to travel for all of them based on following condition : 
# a. Children below 12 = 30% discount 
# b. Senior citizen (above 59) = 50% discount 
# c. Others need to pay full. 

total_amount = 0

for i in range(1, 6):
    print(f"\nPerson {i}")
    
    age = int(input("Enter age: "))
    ticket = float(input("Enter ticket amount: "))

    if age < 12:
        discount = ticket * 0.30
        final_amount = ticket - discount
        print("30% Child Discount Applied")

    elif age > 59:
        discount = ticket * 0.50
        final_amount = ticket - discount
        print("50% Senior Citizen Discount Applied")
        
    else:
        discount = 0
        final_amount = ticket
        print("No Discount")

    print("Amount to Pay =", final_amount)

    total_amount += final_amount


print("Total Ticket Amount =", total_amount)