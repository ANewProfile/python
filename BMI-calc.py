from coolprint import *

height = float(input("Enter your height(meters): "))
weight = float(input("Enter your weight(kg): "))

bmi = weight/(height**2)

def get_obesity(bmi):
    if bmi < 18.5:
        return 'underweight. EAT MORE!!!'
    elif bmi >= 18.5 and bmi < 25:
        return 'just an average joe.'
    elif bmi >= 25 and bmi < 30:
        return 'slightly overweight. You should get some exercise.'
    elif bmi >= 30 and bmi < 35:
        return 'obese. You\'re an average couch potato.'
    elif bmi >= 35:
        return 'clinically obese. Don\'t eat for a month(at least).'

obesity = get_obesity(bmi)
print(f"Your BMI(Body Mass Index) is {bmi}, you are {obesity}")

