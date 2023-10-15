print("BMI calculator")
weight = float(input("Enter your weight in kg: \n"))
height = float (input("Enter your height in m: \n"))
bmi = weight / (height ** 2)
print("Your BMI is: " + str(bmi))

#print(type(bmi))