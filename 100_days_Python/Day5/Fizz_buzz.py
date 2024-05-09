''' if a number is divisible by 3 you say fizz and if the number is divisble
by 5, you say Buzz
'''

for i in range(1,101,1):
    if i%3 ==0:
        print("Fizz")
    elif i%5==0:
        print("Buzz")
    else:
        print(i)