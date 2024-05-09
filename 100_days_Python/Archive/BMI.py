height = float(input(" Please enter your height in metres  "))
weight = float(input(" Please enter your weight in Kilogram  "))
BMI = float(weight/(height**2))
print(f"Your BMI is {BMI}")

if BMI <18.5:
    print(" You are underweight, please see the doctor")
elif BMI > 18.5 and BMI <25:
    print("You have normal weight")
elif BMI > 25 and BMI < 30:
    print("your weight is slightly over weight")
elif BMI > 30 and  BMI < 35:
    print("The BMI looks like for a Obese person")
else:
    print("Please consult the doctor as your BMI is coming as  Clinicaly obese")


