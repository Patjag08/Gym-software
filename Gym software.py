import os
import sys
path = sys.path[0]
clear = lambda: os.system('cls')
Exercise_level_mod = {
    "Little" : 1.2,
    "Light" : 1.375,
    "Moderate" : 1.55,
    "Heavy" : 1.725,
    "Intense" : 1.9
}
#FUNCTIONS
#HEIGHT ONLY IN METERS
def BMI_calc(weight,height):
    return weight / ((height / 100) * (height / 100))
def BMR_calc_men(weight,height,age):
    return 88.362 + (13.397 * weight) + (4.799 * height - (5.677 * age))
def BMR_calc_women(weight,height,age):
    return 447.593 + (9.247 * weight) + (3.098 * height - (4.330 * age))
#PROCEDURES
def aqcuire_member_info():
    global age_input
    global weight_input
    global height_input
    global gender_input
    global exercise_input
    age_valid = False
    weight_valid = False
    height_valid = False
    gender_valid = False
    exercise_valid = False
    age_input = ""
    weight_input  = ""
    height_input = ""
    gender_input = ""
    exercise_input = ""
    while age_valid == False:
        age_input = input("INPUT MEMBERS AGE: ")
        if age_input.isnumeric():
            if int(age_input) >= 14 and int(age_input) <= 100:
                age_valid = True
                clear()
            else:
                print("Invalid range")
        else:
            print("Invalid format")
    while weight_valid == False:
        weight_input = input("INPUT MEMBERS WEIGHT (KG) (ROUNDED TO WHOLE NUMBER): ")
        if weight_input.isnumeric():
            if int(weight_input) >= 30 and int(weight_input) <= 250:
                weight_valid = True
                clear()
            else:
                print("Invalid range")
        else:
            print("Invalid format")
    while height_valid == False:
        height_input = input("INPUT MEMBERS HEIGHT (CM): ")
        if height_input.isnumeric():
            if int(height_input) >= 120 and int(height_input) <= 210:
                height_valid = True
                clear()
            else:
                print("Invalid range")
        else:
            print("Invalid format")
    while gender_valid == False:
        gender_input = input("INPUT MEMBERS GENDER (M/F): ")
        if gender_input.lower() == "m" or gender_input.lower() == "f":
            gender_valid = True
            clear()
        else:
            print("Wrong format")
    while exercise_valid == False:
        print("(1)LITTLE")
        print("(2)LIGHT")
        print("(3)MODERATE")
        print("(4)HEAVY")
        print("(5)INTENSE")
        exercise_input = input("INPUT MEMBERS EXERCISE LEVEL: ")
        if exercise_input.isnumeric():
            if int(exercise_input) >= 1 and int(exercise_input) <= 5:
                exercise_valid = True
                clear()
                if int(exercise_input) == 1:
                    exercise_input = "Little"
                elif int(exercise_input) == 2:
                    exercise_input = "Light"
                elif int(exercise_input) == 3:
                    exercise_input = "Moderate"
                elif int(exercise_input) == 4:
                    exercise_input = "Heavy"
                elif int(exercise_input) == 5:
                    exercise_input = "Intense"
            else:
                print("Out of bounds")
        else:
            print("Wrong format")
#MAIN LOOP
while True:
    clear()
    member_bmi = 0
    member_bmr = 0
    member_maintain = 0
    underweight = False
    normal_weight = False
    Overweight = False
    obese = False
    ideal_member = False
    aqcuire_member_info()
    #CONVERSIONS
    weight_input = int(weight_input)
    height_input = int(height_input)
    age_input = int(age_input)
    #BMR Calculations
    if gender_input.lower() == "f":
        member_bmr = BMR_calc_women(weight_input, height_input, age_input)
        member_maintain = member_bmr * Exercise_level_mod[exercise_input]
    else:
        member_bmr = BMR_calc_men(weight_input, height_input, age_input)
        member_maintain = member_bmr * Exercise_level_mod[exercise_input]
    #BMI Calculations
    member_bmi = BMI_calc(weight_input,height_input)
    #Result creation + catagory
    name = input("ENTER NAME OF MEMBER: ")
    clear()
    result = f"Name: {name}|Height {height_input}|Age {age_input}|Weight {weight_input}|BMI {round(member_bmi,1)}|BMR {round(member_bmr,2)}|Maintain calories: {round(member_maintain)}KCAL"
    if member_bmi < 18.5:
        underweight = True
        result = result + "|Underweight"
    elif member_bmi >= 18.5 and member_bmi <=24.9:
        normal_weight = True
        result = result + "|Normal weight"
    elif member_bmi >= 25 and member_bmi <=29.9:
        Overweight = True
        result = result + "|Overweight"
    elif member_bmi >= 30:
        obese = True
        result = result + "|Obese"
    if round(member_bmi) == 22:
        ideal_member = True
        result = result + "|Ideal BMI"
    else:
        if weight_input-(22 * (height_input*height_input)) < 0:
            result = result + f"|To acheive ideal lose: {round((22 * ((height_input / 100)*(height_input / 100)))-weight_input)}KG"
        else:
            result = result + f"|To acheive ideal gain: {round(weight_input-(22 * ((height_input / 100)*(height_input / 100))))}KG"
    #Writing to file
    print("CALCULATED INFO: ")
    print(result)
    input("PRESS ENTER TO PROCEED")
    file = open(f"{path}\{name+str(age_input)}.txt","w")
    file.writelines(result)
    file.close()