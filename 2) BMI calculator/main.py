lbs_to_kg_multiplication = 0.45359237


def choose_weight():
    weight_type = input("what weight system do you use? (lbs/kgs) \n")
    weight_value = float(input("what is your weight? \n"))
    if weight_type == "lbs":
        return weight_value * lbs_to_kg_multiplication
    else:
        return weight_value


def choose_height():
    height_type = input("what height system do you use? (feet/meters) \n")
    if height_type == "feet":
        height_value_feet = int(input("how many feet? \n"))
        height_value_inches = int(input("inch? \n"))
        return ((height_value_inches + (height_value_feet * 12)) * 2.54) / 100
    else:
        return (float(input("whats you height? (in CM) \n"))) / 100


def calculate_bmi(weight, height):
    return weight / (height ** 2)


def bmi_interpretation(bmi_value):
    if bmi_value < 18.5:
        return "underweight"
    elif bmi_value < 25:
        return "normal weight"
    elif bmi_value < 30:
        return "overweight"
    elif bmi_value < 35:
        return "obese"
    else:
        return "clinically obese"


if __name__ == '__main__':
    print("Welcome to the BMI calculator")
    weight_in_kg = choose_weight()
    height_in_m = choose_height()
    bmi = round(calculate_bmi(weight_in_kg, height_in_m), 2)
    print(f"Your bmi is {bmi}. It means hat you are {bmi_interpretation(bmi)}")
