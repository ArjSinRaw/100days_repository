total_height = 0
no_of_student = 0
student_heights = [ 153, 150, 144, 130, 165]

for height in student_heights:
    total_height += height
print(f"Total height of the student shall be {total_height}")

for student in student_heights:
    no_of_student += 1
print(f"Total student shall be {no_of_student}")

average_height = total_height/no_of_student
print(f"Average height of the student from the lot is {average_height}")