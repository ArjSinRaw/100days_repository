# name = "Veeransh"
# print(type(name))
# print(type(object))
# greeting = "gutenAbend from Germany"
# print(greeting[5])
# print(greeting + name)
# print(greeting[0:2])
# print(greeting[0:8:2])
# print(len(greeting))
# print(greeting.endswith("Germany")) # share boolena response in case of being right
# print(greeting.count('G'))
# print(greeting.capitalize())
# print(greeting)
# print(greeting.find('G'))



#Practice Set solving

#Write a program with user input name followed by Goodafternoon

# a = str(input(" Please enter your name\n "))
# print("Mr/Ms/Mrs", a, " Good Afternoon")


#Write  a program to create the template for the mail

# letter = '''Dear |<NAME>|

# Greetings from Google, US!

# Congratulation, you are selected for the role fo Director of Engineering

# Date :|<DATE>|
# '''

# name = input(" Enter you name \n")
# date = input("Enter today's date please\n")
# letter = letter.replace("|<NAME>|", name)
# letter = letter.replace("|<DATE>|", date)
# print(letter)



#Write a program to detect double space

Stringer = "Once upon a time there was a Sage bathing in the river Ganga and mouse fell into his   hand"
s = Stringer.find(" ")
print(s)

