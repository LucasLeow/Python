# Assuming live until 90 years old
# tells how many days, weeks, months left
# 1 year = 365 days = 52 weeks = 12 months

current_age = int(input("What is your current age: "))
years_remaining = 90 - current_age

months_remaining = years_remaining * 12
weeks_remaining = years_remaining * 52
days_remaining = years_remaining * 365

print(
    f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left")
