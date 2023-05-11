def tip_calculator():
    while True:
        try:
            total_bill = float(input("What was the total bill? $"))
            no_of_people = int(input("How many people to split the bill? "))
            tip = int(input("Want to leave a tip? (choose a percentage, 0 for no tip) %" ))
            ppp = ((total_bill + (total_bill * (tip / 100))) / no_of_people)
            return ppp
        except ValueError:
            print("please make sure you insert numbers only!")


if __name__ == '__main__':
    print ("Welcome to the tip calculator!")
    print(f'Each person needs to pay ${tip_calculator()}')
