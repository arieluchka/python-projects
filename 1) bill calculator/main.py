print ("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
no_of_people = int(input("How many people to split the bill? "))
tip = int(input("Want to leave a tip? (choose a percentage, 0 for no tip) %" ))

# payment per person
ppp = ((total_bill + (total_bill * (tip / 100))) / no_of_people)
print(f'Each person needs to pay ${ppp}')
