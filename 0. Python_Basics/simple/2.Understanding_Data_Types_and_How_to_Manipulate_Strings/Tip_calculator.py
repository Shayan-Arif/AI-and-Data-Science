print("WElcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))
total_bill = bill + (bill * tip / 100)
bill_per_person = total_bill / people
print(f"Each person should pay: ${round(bill_per_person, 2)}")