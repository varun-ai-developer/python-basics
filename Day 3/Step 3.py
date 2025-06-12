def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

w = float(input("Enter your weight in kg: "))
h = float(input("Enter your hieght in meters: "))

bmi = calculate_bmi(w, h)
print("Your BMI is:", round(bmi, 2))

if bmi < 18.5:
    print("You are underweight. ")
elif bmi < 25:
    print("You have a normal weight.")
else:
    print("You are overweight.")
