
print("Welcome to the tip calculator!")


bill1 = float(input ("What was the total bill? $"))
bill2 = int(input ("How much tip would you like to give? 10, 12, or 15? "))
split = int(input("How many people to split the bill? "))
percent = bill2 / 100
tip_amount = bill1 * percent
total_bill = bill1 + percent
bill_per_person = total_bill / split
final_amount = round(bill_per_person, 2)

print(f"Each person should pay: ${final_amount}")
