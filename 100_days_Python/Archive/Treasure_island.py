
print('''
  *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
********************************************************************************
      ''')
print("Welcome to the Treasure Island, I am sure you shall have fun here  ")
print("Your mission is to find the real TREASURE")
choice1 = input("You are at the crossroads, please select 'left' or 'right  ").lower()
if choice1 == 'left':
    choice2 = input("You have crossed the first hurdle and near the river, please type 'swim' or 'wait' for the next steps   ").lower()
    if choice2 ==' wait':
        choice3 = input("You have succesfully crossed the islant, please choose the door you want to enter now i.e 'Blue' or 'red' or 'yellow   ").lower()
        if choice3 =='yellow':
            print("You have found the treasure")
        else:
            print("Hard Luck, you have reached so far but still couldn't make it")
    else :
            print("You have drowned in the river")  
else :
    print("You fell into the hole, game is over!")


