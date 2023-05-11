class BmiCalculator:

    def __init__(self):
        self._height = None
        self._weight = None
        self._bmi_value = None
        self._lbs_to_kg_multiplication = 0.45359237

    def choose_weight(self):
        weight_type = input("what weight system do you use? (lbs/kgs) \n")
        weight_value = float(input("what is your weight? \n"))
        if weight_type == "lbs":
            self._weight = weight_value * self._lbs_to_kg_multiplication
            return self._weight
        else:
            self._weight = weight_value
            return self._weight

    def choose_height(self):
        height_type = input("what height system do you use? (feet/meters) \n")
        if height_type == "feet":
            height_value_feet = int(input("how many feet? \n"))
            height_value_inches = int(input("inch? \n"))
            self._height = ((height_value_inches + (height_value_feet * 12)) * 2.54) / 100
            return self._height
        else:
            self._height = (float(input("whats you height? (in CM) \n"))) / 100
            return self._height

    def calculate_bmi(self):
        self._bmi_value = round((self._weight / (self._height ** 2)), 2)
        return self._bmi_value

    # added the option to call the method while input a known bmi,
    # to skip the whole calculating progress

    def bmi_interpretation(self, bmi=None):
        if bmi is None:
            bmi = self._bmi_value
        if bmi < 18.5:
            return "underweight"
        elif bmi < 25:
            return "normal weight"
        elif bmi < 30:
            return "overweight"
        elif bmi < 35:
            return "obese"
        else:
            return "clinically obese"


if __name__ == '__main__':
    print("Welcome to the BMI calculator")
    bmi_check = BmiCalculator()
    bmi_check.choose_weight()
    bmi_check.choose_height()
    print(f"Your bmi is {bmi_check.calculate_bmi()}. It means hat you are {bmi_check.bmi_interpretation()}")
