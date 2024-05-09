print("The LOVE CALCULATOR is calculating your score ")

your_name = input("Please enter your name  ")
love_name = input("Please input your love's name ")
combined_name = your_name + love_name
lower_name = combined_name.lower()

t = lower_name.count('t')
r = lower_name.count('r')
u = lower_name.count('u')
e = lower_name.count('e')
first_digit = t+r+u+e

l = lower_name.count('l')
o = lower_name.count('o')
v = lower_name.count('v')
e = lower_name.count('e')
second_digit = l+o+v+e

love_score = int(str(first_digit) + str(second_digit))

if love_score <10 and love_score >90:
    print(f"Your score is {love_score}; You go together like coke and mentos")
elif love_score >= 40 and love_score <=50:
    print(f"Your score is {love_score}; you are alright together")
else :
    print(f"You score is {love_score}")
