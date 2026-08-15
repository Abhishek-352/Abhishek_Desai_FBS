# Write a program to convert days into years, weeks and days.

total_days = int(input("Enter total number of days: "))

years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7

print("\n"f"In toal days {total_days} there are {years} years, {weeks} weeks and {days} remaining days")
