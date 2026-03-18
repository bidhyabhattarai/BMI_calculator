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

# use  loopto calculate bmi of 3 people 
stashed_data = []
for i in range(3):
    name = input("\nEnter name: ")
    weight = float(input("Enter weight in kg: "))
    height = float(input("Enter height in meters: "))
    bmi = weight / (height * height)
    stashed_data.append((name, bmi))
print("\n------ BMI REPORT FOR 3 PEOPLE ------")
for name, bmi in stashed_data:
    print(f"{name}: BMI = {round(bmi, 2)}")