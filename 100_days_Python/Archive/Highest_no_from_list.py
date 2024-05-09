max_score = 0
student_marks = [45,100, 33901, 9, 55, 3390, 345, 8,80]
for score in student_marks:
    if score > max_score:
        max_score = score
print(f"Your max score is {max_score}")

total_sum = 0
#for i in range(101): also the same result as below for loop here
for i in range(1,101,1):    
    total_sum +=i
print(f"Total sum of number from 1 to 100 is {total_sum}")
