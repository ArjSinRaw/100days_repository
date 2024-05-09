print("Welcome to the roller coaster ride")
height_of_the_guest = int(input("Please enter your height  "))
bill = 0

if height_of_the_guest >= 120:
    print("You are eligible to join the rollercoaster ride")
    age = int(input("Please enter your age  "))
    if age < 12 :
        bill = 5
        print(f"Your bill for the ride is ${bill}")
    elif age <= 18:
        bill = 10
        print(f"Your bill for the ride is ${10}")
    elif age >= 45 and age <=55:
        bill = 0
        print(f"Everything on us, It's okay")
    else :
        bill = 10
        print(f"Your bill for the rider shall be ${bill}")

    wants_photo = input("Do you want the photos as well. Please enter 'Y' or 'N' ").upper()
    while True:
        if wants_photo in ['Y','N']:
            break
        else:
            print("Please enter valide input i.e type 'Y" or'N')
    if wants_photo == 'Y':
        bill +=3
        print(f"Your bill amount for the rider shall be {bill}")
else :
    print("You are not eligible for the ride")