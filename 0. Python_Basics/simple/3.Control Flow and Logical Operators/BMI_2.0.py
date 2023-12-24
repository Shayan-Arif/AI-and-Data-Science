print("BMI calculator")
weight = float(input("Enter your weight in kg: \n"))
height = float (input("Enter your height in m: \n"))
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))
if bmi < 18.5:
    print("You are underweight.")
elif bmi < 25:
    print("You have a normal weight.")
elif bmi < 30:
    print("You are slightly overweight.")
elif bmi < 35:
    print("You are obese.")
else:
    print("You are clinically obese.")