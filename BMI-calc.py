height = float(input("Enter your height(meters): "))
weight = float(input("Enter your weight(kg): "))

square_height = height * height
bmi = square_height/weight

print(f"Your BMI(Body Mass Index) is {bmi}")
