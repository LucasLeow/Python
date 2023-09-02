height = input("Enter your height in meters: ")
weight = input("Enter your weight in kg: ")
bmi = float(weight) / (float(height) ** 2)
print(f"Your BMI is: {round(bmi, 2)}")
if (bmi < 18.5):
    print("You are underweight")
elif (bmi >= 18.5 and bmi < 25):
    print("You are normal weight")
elif (bmi >= 25 and bmi < 30):
    print("You are overweight")
elif (bmi >= 30 and bmi < 35):
    print("You are obese")
else:
    print("You are clinically obese")
