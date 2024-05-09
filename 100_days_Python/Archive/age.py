print(" Welcome to the Tip Calculator")
bill_amount = float(input(" Please enter the total bill amount "))
tip_amount = float(input("Please enter the tip amount "))
no_of_people = int(input("How many people would share the bill  "))
share_per_person =round(( bill_amount + tip_amount)/no_of_people, 2)
print(f"Each individual needs to pay {share_per_person} dollars ")
44