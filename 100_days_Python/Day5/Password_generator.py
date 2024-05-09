import random 
numbers=  [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
symbol =  ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '{', '}', '[', ']', '|', '\\', ';', ':', '"', "'", '<', '>', ',', '.', '?', '/']
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

print("Welcome to the password generator")
nr_letter = int(input("Please enter the number of letter you want in the password \n"))
nr_symbol = int(input("Please enter the number of symbol you want in the password \n"))
nr_number= int(input("Please enter the number of numbers you want in the password \n"))

password = ''


for char in range(1,nr_letter+1,1):
    password +=random.choice(alphabets)
for char in range(1,nr_symbol+1,1):
    password +=random.choice(symbol)
for char in range(1,nr_number+1,1):
    password +=str(random.choice(numbers))

print(password)

password_list = list(password)
random.shuffle(password_list)
password = ''.join(password_list)
print(password)

# print(password_list)