print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill?"))
tip_pct = float(
    input("What percentage of tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))
bill_per_pax = (total_bill * (1 + (tip_pct/100))) / num_people
print(f"Each person should pay: ${round(bill_per_pax, 2)}")
