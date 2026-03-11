# Task 1: Ask user input and print it
name = input("What is your name? ")
weight = float(input("What is your weight in kg? "))
height = float(input("What is your height in meters? "))
print("Your name is " + name + "\nyour weight is " + str(weight) + " kg and, \nyour height is " + str(height) + " meters.")

# print weight and height data types using type(). 
print("The data type of weight is: " + str(type(weight)))
print("The data type of height is: " + str(type(height)))

# Calculate BMI
bmi = weight / (height * height)

# Print BMI result
print("Your BMI is: " + str(bmi))

# Categories
if bmi < 18.5:
    category = "Underweight"
elif bmi <= 24.9:
    category = "Normal"
elif bmi <= 29.9:
    category = "Overweight"
else:
    category = "Obese"

# Display formatted BMI report
print("\n------ BMI REPORT ------")
print("Name   :", name)
print("Weight :", weight, "kg")
print("Height :", height, "m")
print("BMI    :", round(bmi, 2))
print("------------------------")
